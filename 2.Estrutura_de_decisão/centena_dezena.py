
# Programa que calcula: centena, dezena e unidade

num = input("\nDigite um numero menor que 1000 \n")
numStr = str(num)
qtNumero = len(numStr)

if qtNumero == 3:
    centena = numStr[0:1]
    dezena = numStr[1:2]
    unidade = numStr[2:3]
    print (numStr+" = "+centena+" centenas , "+dezena+" dezenas, "+unidade+ " unidades")

if qtNumero == 2:
    dezena = numeroStr[0:1]
    unidade = numeroStr[1:2]
    print (numeroStr+" = "+dezena+" dezenas, "+unidade+ " unidades")

if qtNumero == 1:
    unidade = numeroStr[0:1]
    print (numeroStr+" = "+unidade+ " unidades")
if qtNumero >= 4:
    print("\nNumero inválido!")

enter = input("\nPressione <Enter> para encerrar...")

"""numero = input("digite um numero menor que 1000 ---> ")"""