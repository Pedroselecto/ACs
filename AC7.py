# Exercício 1: Salary increase
def aumento():
    salario = float(input())
    if salario >= 0.00 and salario <= 400.00:
        percentual = 0.15
        reajuste = percentual * salario
        salario_novo = reajuste + salario
        print("Novo salario: {:.2f}".format(salario_novo))
        print("Reajuste ganho: {:.2f}".format(reajuste))
        print("Em percentual: 15 %")

    if salario >= 400.01 and salario <= 800.00:
        percentual = 0.12
        reajuste = percentual * salario
        salario_novo = reajuste + salario
        print("Novo salario: {:.2f}".format(salario_novo))
        print("Reajuste ganho: {:.2f}".format(reajuste))
        print("Em percentual: 12 %")

    if salario >= 800.01 and salario <= 1200.00:
        percentual = 0.1
        reajuste = percentual * salario
        salario_novo = reajuste + salario
        print("Novo salario: {:.2f}".format(salario_novo))
        print("Reajuste ganho: {:.2f}".format(reajuste))
        print("Em percentual: 10 %")

    if salario >= 1200.01 and salario <= 2000.00:
        percentual = 0.07
        reajuste = percentual * salario
        salario_novo = reajuste + salario
        print("Novo salario: {:.2f}".format(salario_novo))
        print("Reajuste ganho: {:.2f}".format(reajuste))
        print("Em percentual: 7 %")

    if salario > 2000.00:
        percentual = 0.040
        reajuste = percentual * salario
        salario_novo = reajuste + salario
        print("Novo salario: {:.2f}".format(salario_novo))
        print("Reajuste ganho: {:.2f}".format(reajuste))
        print("Em percentual: 4 %")

#aumento()

# Exercício 2: Even Between five Numbers

def valores_pares():
    numeros_pares = 0
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    if num1 % 2 == 0:
        numeros_pares = numeros_pares + 1
    if num2 % 2 == 0:
        numeros_pares = numeros_pares + 1
    if num3 % 2 == 0:
        numeros_pares = numeros_pares + 1
    if num4 % 2 == 0:
        numeros_pares = numeros_pares + 1
    if num5 % 2 == 0:
        numeros_pares = numeros_pares + 1
    print(numeros_pares, "valores pares")

#valores_pares()

# Exercício 3: Multiples of 13
def soma():
    x = int(input())
    y = int(input())
    valor = 0
    if x > y:
        for num in range(y, x+1):
            if num % 13 == 0:
                continue
            valor += num
    else:
        for num in range(x, y+1):
            if num % 13 == 0:
                continue
            valor += num
    print(valor)
#soma()

# Exercício 4: Array fill I

def array():
    v = int(input())
    for num in range(0, 10):
        print("N[{}] = {}".format(num, v))
        v *= 2

#array()

# Exercício 5: Lowest Number and Position
def menor():
    N = int(input())
    lista = [int(i) for i in input().split()]
    achar_menor = [int(num) for num in lista]
    achar_menor.sort()
    print("Menor valor:", achar_menor[0])
    print("Posicao:", lista.index(achar_menor[0]))

#menor()

# Exercício 6: Column in Array

def matriz():
    C = int(input())
    operacao = input().upper()
    soma = 0
    media = 0
    matriz = []
    for _ in range(0, 144):
        matriz.append(float(input()))
    if operacao == "S":
        for _ in range(0, 12):
            soma += matriz[C]
            C += 12
        print("{:.1f}".format(soma))
    if operacao == "M":
        for _ in range(0,12):
            media += matriz[C]
            C += 12
        media = media / 12
        print("{:.1f}".format(media))

#matriz()

# Exercício 7: Sort by lenght

def sortear():
    n = int(input())
    for _ in range(0, n):
        frases = input()
        frases = frases.split(" ")
        frases.sort(key=len, reverse=True)
        print(" ".join(frases))

#sortear()

