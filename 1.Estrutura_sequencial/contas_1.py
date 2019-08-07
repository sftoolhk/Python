# Diversos calculos com numeros colocados pelo usuario

num1 = int(input("Entre com um numero inteiro: "))
num2 = int(input("Entre com um numero inteiro: "))
num3 = float(input("Entre com um numero real: "))
produto = (num1 * 2) * (num2 / 2)
soma = (num1 * 3) + num3
elevado = num3 ** 3
print("\nO produto do dobro do primeiro e metade do segundo é: %s" % produto)
print("\nA soma do triplo do primeiro com o terceiro é: %s" % soma)
print("\nO terceiro numero elevado ao cubo é: %s" % elevado)

enter = input("\nPressione <Enter> para encerrar...")