import rpyc
HOST = 'localhost'

def check_for_process_connection(processes, port):
    try:
        if port not in processes:
            processes[port] = rpyc.connect(HOST, port)
        return True
    except:
        return False

def main():
    processes = {}
    while True:
            op = input("Digite uma operacao('show', 'search', 'insert', 'show ring', 'fim' para terminar):\n")
            if op == 'fim':
                for k in processes.keys():
                    processes[k].close()
                break
            elif op == 'show':
                port = int(input("Digite qual a porta do nó que deseja mostrar:"))
                if check_for_process_connection(processes, port):
                    print(processes[port].root.identifier())
                else:
                    print("A porta inserida não corresponde a um nó válido")
            elif op == 'show ring':
                port = int(input("Digite qual a porta do nó que deseja questionar sobre o anel:"))
                if check_for_process_connection(processes, port):
                    print(processes[port].root.get_ring())
                else:
                    print("A porta inserida não corresponde a um nó válido")
            elif op == 'search':
                key = input("Qual chave deseja buscar? ")
                port = int(input("A busca deve ser feita a partir de qual nó(digite a porta)? "))
                if check_for_process_connection(processes, port):
                    ans = processes[port].root.search_identifier(key)
                    if ans:
                        print('Encontrado na posição', ans[0], '-', ans[1])
                    else:
                        print('Chave não encontrada')
                else:
                    print("A porta inserida não corresponde a um nó válido")
            elif op == 'insert':
                key = input("Qual chave deseja inserir? ")
                value = input("Qual o conteúdo que deseja inserir (valor)? ")
                port = int(input("A inserção deve ser feita a partir de qual nó(digite a porta)? "))
                if check_for_process_connection(processes, port):
                    print("Chave inserida na posição:", processes[port].root.insert(key, value))
                else:
                    print("A porta inserida não corresponde a um nó válido")
if __name__ == "__main__":
    main()
