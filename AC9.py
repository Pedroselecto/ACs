# Exercício 1: Distance

def distancia():
    distancia = int(input())
    y = 30
    tempo = distancia / y
    minutos = tempo * 60
    print("{:.0f} minutos".format(minutos))

#distancia()

# Exercício 2: Simple Factorial

from math import factorial

def fatorial():
    n = int(input())
    print(factorial(n))

#fatorial()

# Exercício 3: Going to the Market

def frutas():
    N = int(input())
    for _ in range(N):
        produtos = {}
        custo = 0
        quantia = int(input())

        for _ in range(quantia):
            produto = input().split()
            produtos[produto[0]] = float(produto[1])

        lista_produtos =  int(input())
        for _ in range(lista_produtos):
            fruta, quantidade = input().split()
            if fruta in produtos.keys():
                custo += produtos[fruta] * int(quantidade)
        print("R$ {:.2f}".format(custo))

#frutas()

# Exercício 4: Identifying Tea

def cha():
    tipo = int(input())
    respostas = [int(n) for n in input().split()]
    acertos = respostas.count(tipo)
    print(acertos)

#cha()

# Exercício 5: Aviões de papel
def folhas():
    dados = [int(n) for n in input().split()]
    if dados[0] * dados[2] <= dados[1]:
        print("S")
    else:
        print("N")

#folhas()

# Exercício 6: Tacógrafo

def tacografo():
    intervalos = int(input())
    distancia = 0
    for _ in range(intervalos):
        dados = [int(n) for n in input().split()]
        distancia += dados[0] * dados[1]
    print(distancia)

#tacografo()

# Exercício 7: Busca na internet

def clicks():
    terceiro = int(input())
    segundo = terceiro * 2
    primeiro = segundo * 2
    print(primeiro)

#clicks()

# Exercício 8: Sequência secreta

def sequencia():
    n = int(input())
    lista = []
    total = 1
    for _ in range(n):
        num = int(input())
        lista.append(num)
    item_anterior = lista[0]
    for item in lista:
        if item_anterior == item:
            continue
        else:
            total += 1
        item_anterior = item
    print(total)

sequencia()