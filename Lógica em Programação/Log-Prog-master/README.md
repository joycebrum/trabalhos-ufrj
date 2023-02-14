# Verificador Lógica Modal.

#### Programa recebe uma fórmula modal, um grafo e retorna o valor booleano da formula.
#### Feito por Joyce Brum e Thiago Outeiro

### Arquivo a ser executado na shell do python:
    main.py

### Método a ser chamado: 
    valor (estados, relacoes, valoracao, estado, f) - para verifica a função f a partir de estado em um grafo especificado na entrada 
    
    ou 
    
    verifica(estado, f) - para verificar a funcao f a partir do estado no grafo default já implementado

### Parâmetros: 

estados, relacoes, valoracao, estado, f

- #### estados:
    Array de strings onde cada string representa o nome de um estado.
- #### relacoes:
    Mapa onde no seguinte formato: { 
                                     chave: tipo(string)
                                     valor: { 
                                                chave: estado (string)
                                                valor: lista de estados vizinhos do estado
                                             }
                                    }
- #### valoracao:
    Mapa onde as chaves são as variáveis e os valores associados a elas são um array de estados nos quais a variavel é verdadeira.
- #### estado:
    String com o estado desejado.
- #### f:
    String com operadores:
    
    | Símbolo  | Significado |
    | ------------- | ------------- |
    | <b>`!`</b>  | Negação  |
    | <b>`->`</b>  | Implicação  |
    | <b>`\|`</b>  | Ou  |
    | <b>`&`</b>  | E  |
    | <b>`[a]`</b>  | Para todo vizinho 'a'  |
    | <b>`<a>`</b>  | Existe um vizinho 'a' |

### Exemplo default implementado

Para facilitar, colocamos um exemplo ja pronto, que esta desenhado na imagem: "Especificação/Grafo Logica(1)", segue um exemplo de sucesso e de falha

    estados = ["012", "021", "102", "120", "210", "201"]

    relacoes = {
         "ana": {
                    "012": ["021"], "021": ["012"],
                    "102": ["120"], "120": ["102"],
                    "210": ["201"], "201": ["210"]
                 },
         "beto": {
                    "012": ["210"], "210": ["012"],
                    "102": ["201"], "201": ["102"],
                    "021": ["120"], "120": ["021"]
                  },
         "carla": {
                    "012": ["102"], "102": ["012"],
                    "021": ["201"], "201": ["021"],
                    "120": ["210"], "210": ["120"]
                  }
          }

    valoracao = {
                    "0a": ["012", "021"], 
                    "0b": ["102", "201"], 
                    "0c": ["120", "210"],
                    "1a": ["120", "102"], 
                    "1b": ["210", "012"], 
                    "1c": ["021", "201"],
                    "2a": ["201", "210"], 
                    "2b": ["021", "120"], 
                    "2c": ["012", "102"]
                }

##### Exemplo com resultado true:
    
###### Formula escrita:

    verifica("012", "[ana]<beto>[carla](2a & 1b)")
    

##### Exemplo com resultado false
    
###### Formula escrita:
    
    verifica("012", "[ana]<beto>(!2b & [carla](2a & 1b))")
 
# Verificador Modelos

### Executando exemplo 1
Abra o prompt de comando na pasta "Verificação de Modelo" e execute a seguinte linha de codigo:
    
    nuXmv -source commands example1

A saída mostrará passo a passo da simulação do verificador.
    
### Executando exemplo 2
Abra o prompt de comando na pasta "Verificação de Modelo" e execute a seguinte linha de codigo:
    
    nuXmv -source commands example2

A saída mostrará passo a passo da simulação do verificador.

