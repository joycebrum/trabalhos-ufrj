
import constant

funcao = ""
contador = 0

def transformaFormula(f):
    global funcao
    funcao = f
    if f:
        result = parse(0)
        return result
    return []

def parse(pos):
    global funcao
    global contador
    parseado = []
    i = pos
    #for i in range( pos, len(funcao)):
    variavel = ""
    while i < len(funcao):
        if funcao[i] == '*':
            while i < len(funcao) and funcao[i] != ')':
                i = i + 1
        elif(funcao[i] == '('):
            variavel = adicionaVariavel(variavel, parseado)
            subarray = parse(i+1)
            parseado.append(subarray)
        elif(funcao[i] == ')'):
            variavel = adicionaVariavel(variavel, parseado)
            funcao = funcao.replace(funcao[pos:i], "*" + str(contador))
            contador += 1
            return parseado
        elif i+1 < len(funcao) and(funcao[i] + funcao[i+1]) == constant.IMPLICACAO:
            variavel = adicionaVariavel(variavel, parseado)
            parseado.append(constant.IMPLICACAO)
            i = i + 1
        elif funcao[i] == constant.PARATODOINICIO or funcao[i] == constant.ALGUMINICIO:
            variavel = adicionaVariavel(variavel, parseado)
            i, subarray = adicionaParaTodoEExiste(i) 
            parseado.append(subarray)
        elif funcao[i] == constant.AND or funcao[i] == constant.OR or funcao[i]== constant.NOT :
            variavel = adicionaVariavel(variavel, parseado)
            parseado.append(funcao[i])
            
        elif funcao[i] == ' ':
            variavel = adicionaVariavel(variavel, parseado)
        else :
            variavel += funcao[i]
        i = i + 1
    variavel = adicionaVariavel(variavel, parseado)
    return parseado

def adicionaVariavel(variavel, parseado):
    if len(variavel) > 0:
        parseado.append(variavel)
        variavel = ""
    return variavel

def adicionaParaTodoEExiste(pos):
    global contador
    global funcao
    parseado = []
    final = ''
    i = pos
    if(funcao[i] == constant.PARATODOINICIO):
        final = constant.PARATODOFIM
    else:
        final = constant.ALGUMFIM
    parseado.append(funcao[i])
    variavel = ""

    i = nextAndCleanWhiteSpaces(i)
    while i < len(funcao) and funcao[i]!= final and funcao[i]!= ' ':
        variavel += funcao[i]
        i = i + 1
    adicionaVariavel(variavel, parseado)
    i = cleanWhiteSpaces(funcao, i)
    parseado.append(funcao[i]) #final

    i = nextAndCleanWhiteSpaces(i)
    if funcao[i] == '(':
        subarray = parse(i+1)
        parseado.append(subarray)
    elif funcao[i] == constant.PARATODOINICIO or funcao[i] == constant.ALGUMINICIO:
        i, subarray = adicionaParaTodoEExiste(i)
        parseado.append(subarray)
    elif funcao[i] == constant.NOT:
        subarray = []
        subarray.append(funcao[i])
        i = nextAndCleanWhiteSpaces(i)
        if funcao[i] == '(':
            subarray += parse(i);
        elif funcao[i] == constant.PARATODOINICIO or funcao[i] == constant.ALGUMINICIO:
            i, arraytemp = adicionaParaTodoEExiste(i)
            subarray = subarray + arraytemp
        else :
            i = addProposition(i, subarray)
        parseado.append(subarray)
    else :
        i = addProposition(i, parseado)
    return i, parseado

def addProposition(i, parseado):
    global funcao
    variavel = ""
    while i < len(funcao) and isAlphaNum(funcao[i]):
        variavel += funcao[i]
        i = i + 1
    adicionaVariavel(variavel, parseado)
    return i

def removeStrFunction(pos, i) :
    global funcao
    funcao = funcao.replace(funcao[pos:i+1], "") #remove da formula
    return pos

def isAlphaNum(char):
    return (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or (char >= '0' and char <= '9')

def nextAndCleanWhiteSpaces(i):
    global funcao
    i = i + 1 
    return cleanWhiteSpaces(funcao, i)

def cleanWhiteSpaces(funcao, i):
    while i < len(funcao) and funcao[i] == ' ':
        i = i + 1
    return i;
