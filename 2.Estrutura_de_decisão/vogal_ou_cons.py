#Identificar se é vogal ou consoante
letra = input("Digite uma letra do alfabeto: ")
vogais = ('a', 'e', 'i', 'o', 'u')

if letra in vogais:
    print("A letra digitada é uma VOGAL")
else:
    print("A letra é uma CONSOANTE")

enter = input("\nPressione <Enter> para encerrar...")