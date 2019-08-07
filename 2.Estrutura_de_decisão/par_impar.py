# Identificar se o numero é par ou impar
resto = int(input("\nDigite um numero inteiro: "))
par = resto % 2

if (par == 0):
    print("\nO numero digitado é Par")
else:
    print("\nO numero digitado é Impar")

enter = input("\nPressione <Enter> para encerrar...")