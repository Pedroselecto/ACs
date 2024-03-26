# Exercício 1
print("Hello World!")

# Exercício 2
a = int(input())
b = int(input())
x = a + b
print("X =", x)

# Exercício 3
produto1 = input()
info1 = produto1.split(" ")
unidades1 = int(info1[1])
valor1 = float(info1[2])
valorF1 = valor1 * unidades1

produto2 = input()
info2 = produto2.split(" ")
unidades2 = int(info2[1])
valor2 = float(info2[2])
valorF2 = valor2 * unidades2

valorF = valorF1 + valorF2
print("VALOR A PAGAR: R$ {:.2f} ".format(valorF))

# Exercício 4
valores = input()
números = valores.split(" ")
a = int(números[0])
b = int(números[1])
c = int(números[2])
MaiorAB =(a + b + abs(a - b))/2
if MaiorAB > c:
    print("{:.0f} eh o maior".format(MaiorAB))
else:
    print("{:.0f} eh o maior".format(c))

# Exercício 5
valores1 = input()
p1 = valores1.split(" ")
x1 = float(p1[0])
y1 = float(p1[1])
valores2 = input()
p2 = valores2.split(" ")
x2 = float(p2[0])
y2 = float(p2[1])

Distância = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
print("{:.4f}".format(Distância))