# Exercício 1: Collectable cards
from math import gcd
def cartas():
    n = int(input())
    for _ in range(n):
        nums = input()
        valores = nums.split(" ")
        valores = [int(num) for num in valores]
        F1 = valores[0]
        F2 = valores[1]
        print(gcd(F1, F2))

#cartas()

# Exercício 2: Queen

def xadrez():
    while True:
        coordenada = input().split(" ")
        coordenada = [int(num) for num in coordenada]
        if coordenada[0] == 0 and coordenada[1] == 0 and coordenada[2] == 0 and coordenada[3] == 0:
            break
        elif coordenada[0] == coordenada[2] and coordenada[1] == coordenada[3]:
            print(0)
            continue
        elif coordenada[0] == coordenada[2] or coordenada[1] == coordenada[3] or abs(coordenada[0] - coordenada[2]) == abs(coordenada[1] - coordenada[3]):
            print(1)
            continue
        else:
            print(2)
            continue

#xadrez()

# Exercício 3: Factorial Sum

from math import factorial
def soma():
    while True:
        try:
            valores = input().split(" ")
            valores = [int(num) for num in valores]
            n = factorial(valores[0])
            m = factorial(valores[1])
            print(n + m)
        except EOFError:
            return

#soma()

# Exercício 4: Blobs

def blobs():
    casos = int(input())
    for _ in range(casos):
        dias = 0
        comida = float(input())
        while comida > 1:
            comida = comida / 2
            dias = dias + 1
        print(dias, "dias")

#blobs()

# Exercício 5: Number frequence

def frequencia():
    N = int(input())
    lista = []
    for _ in range(N):
        x = int(input())
        lista.append(x)
    unica = list(set(lista))
    unica.sort()
    for n in range(len(unica)):
        print("{} aparece {} vez(es)".format(unica[n], lista.count(unica[n])))

#frequencia()

# Exercício 6: Fast Prime Number

def primos():
    N = int(input())
    for _ in range(N):
        X = int(input())
        raiz = X ** 0.5
        primo = "Prime"
        for i in range(2, int(raiz+1)):
            if X % i == 0:
                primo = "Not Prime"
        else:
            print(primo)

#primos()

# Exercício 7: Head or Tail

def moeda():
    while True:
        N = int(input())
        if N == 0:
            break
        R = input().split()
        print("Mary won {} times and John won {} times".format(R.count("0"), R.count("1")))

#moeda()

# Exercício 8: Functions

def funcoes():
    N = int(input())
    for _ in range(N):
        valores = [int(n) for n in input().split()]
        x = valores[0]
        y = valores[1]
        Rafael = (3 * x)** 2 + y ** 2
        Beto = 2 * (x ** 2) + (5 * y) ** 2
        Carlos = -100 * x + y ** 3
        if Rafael > Beto and Rafael > Carlos:
            print("Rafael ganhou")
        elif Beto > Rafael and Beto > Carlos:
            print("Beto ganhou")
        elif Carlos > Rafael and Carlos > Beto:
            print("Carlos ganhou")

#funcoes()