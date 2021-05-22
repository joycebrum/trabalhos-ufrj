import rpyc
HOST = 'localhost'

def check_for_process_connection(processes, port):
    if port not in processes:
        processes[port] = rpyc.connect(HOST, port)
        
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
                check_for_process_connection(processes, port)
                print(processes[port].root.identifier())
            elif op == 'show ring':
                port = int(input("Digite qual a porta do nó que deseja questionar sobre o anel:"))
                check_for_process_connection(processes, port)
                print(processes[port].root.get_ring())
            elif op == 'search':
                key = input("Qual chave deseja buscar? ")
                port = int(input("A busca deve ser feita a partir de qual nó(digite a porta)? "))
                check_for_process_connection(processes, port)
                ans = processes[port].root.search_identifier(key)
                if ans:
                    print('Encontrado na posição', ans[0], '-', ans[1])
                else:
                    print('Chave não encontrada')
            elif op == 'insert':
                key = input("Qual chave deseja inserir? ")
                value = input("Qual o conteúdo que deseja inserir (valor)? ")
                port = int(input("A inserção deve ser feita a partir de qual nó(digite a porta)? "))            
                check_for_process_connection(processes, port)
                print("Chave inserida na posição:", processes[port].root.insert(key, value))
if __name__ == "__main__":
    main()
