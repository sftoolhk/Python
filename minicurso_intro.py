#-------------------------------------------------------------------------------
# Name:        MiniCurso
# Purpose:     Python Introduce
#
# Author:      cj3002578
#
# Created:     21/05/2019
# Copyright:   (c) cj3002578 2019
# Licence:     PyScripter
#-------------------------------------------------------------------------------

#Entrada
x = int(input("x = "))

#Saída
print(x)

#Deisão
if (x == 0):
    print("x é igual a zero!")

elif (x > 0):
    print("x é maior que zero!")

else:
    print("x é menor que zero!")

#Laços

#for
print()
for i in range(0, x):
    print("x")

#while
print()
i = 0
while i < x:
    print("y")
    i = i + 1

#Função
def func():
    print("Function")
    return

func()

#Classe
class Classe:

    def __init__(self):
        self.y = x

    def print_Y(self):
        print("Classe Y: ", self.y)

z = Classe()

z.print_Y()







