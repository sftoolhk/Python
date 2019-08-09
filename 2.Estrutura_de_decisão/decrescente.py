# Ordenação de numeros na ordem decrescente

a = int(input("\nDigite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

if (a < b):
    a, b = b, a
if (b < c):
    b, c = c, b
if (c > a):
    c, a = a, c

print(a, b, c)

enter = input("\nPressione <Enter> para encerrar...")