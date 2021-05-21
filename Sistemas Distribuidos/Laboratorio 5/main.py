import random
import multiprocessing
import hashlib
import rpyc
from rpyc.utils.server import ThreadedServer

class ChordRing(rpyc.Service):
    exposed_aux = 9
    def on_connect(self, conx):
        self.nodes = [[] for x in range(0,16)]
        print("Conexão estabelecida")
    def on_disconnect(self, conx):
        print("Conexão encerrada")
    def exposed_hash_function(identifier):
        return int(hashlib.sha1(str(identifier).encode('utf-8')).hexdigest(), 16) % 16
    
def get_sha1_key(identifier):
    return int(hashlib.sha1(str(identifier).encode('utf-8')).hexdigest(), 16) % 16

class Process(rpyc.Service):
    exposed_aux = 10
    def on_connect(self, conx):
    	print("Conexao estabelecida.")
    def on_disconnect(self, conx):
    	print("Conexao encerrada.")

def child_process(host, door):
    print('Processo', get_sha1_key(host + str(door)), 'endereço', host, 'porta', door)
    #process = ThreadedServer(Process, port=door)
    #process.start()

def random_door(used_doors):
    door = int(random.uniform(4000, 9000))
    while door in used_doors and len(used_doors) < 9000 - 4000:
        door = int(random.uniform(5010, 7010))
    used_doors[str(door)] = True
    return door

def run_chord():
    chord = ThreadedServer(ChordRing, port = 9100)
    chord.start()

def main():
    processes = []
    n = int(input('Entre com o valor de n: '))
    used_doors = {}
    HOST = '192.168.0.13'

    chord_process = multiprocessing.Process(target=run_chord, args=())
    chord_process.start()

    for i in range(0, n):
        process = multiprocessing.Process(target=child_process, args=(HOST, random_door(used_doors)))
        process.start()
        processes.append(process)
        
    while True:
        op = input("Digite uma operação(list, ou 'fim' para terminar): ")
        if op == 'list':
            for key in used_doors.keys():
                print(HOST, key)
        elif op == 'fim':
            chord_process.terminate()
            chord_process.join()
            for p in processes:
                p.join()
            break

if __name__ == "__main__":
    main()
