import rpyc
def main():
    #calc = rpyc.connect('localhost', 10000)
    #print(calc.root.aux)
    while True:
            op = input("Digite uma operacao(+,-,*,/, ou 'fim' para terminar):")
            if op == 'fim':
                    #calc.close()
                    break

if __name__ == "__main__":
    main()
