import random
import multiprocessing
import rpyc
from rpyc.utils.server import ThreadedServer
import chord as ch
from chord import Process
from chord import ChordRing
import socket

HOST = 'localhost'

def child_process(host, door):
    identifier = host +':' + str(door)
    chord = rpyc.connect(HOST, ch.CHORD_PORT)
    process = ThreadedServer(Process(identifier, chord), port=door)
    process.start()

def main():
    processes = []

    chord_process = multiprocessing.Process(target=ch.run_chord, args=())
    chord_process.start()
    avaiable_ports = [7000, 7001, 7002, 7003, 7005, 7006, 7009, 7010, 7013, 7014, 7018, 7023, 7025, 7049, 7086, 7095]


    for i in range(0, 16):
        port = avaiable_ports[i]
        process = multiprocessing.Process(target=child_process, args=(HOST, port))
        process.start()
        processes.append(process)
        
    while True:
        op = input("Digite uma operação(list, ou 'fim' para terminar): ")
        if op == 'list':
            for port in avaiable_ports:
                print(HOST +':' + str(port))
        elif op == 'fim':
            chord_process.terminate()   
            chord_process.join()
            for p in processes:
                p.terminate()
                p.join()
            break

if __name__ == "__main__":
    main()
