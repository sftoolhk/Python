print('\n')
while (num <= 5):
    num = float(input("Digite um numero "'\n'))
    num -= 1
    
    soma = num + num + num + num + num

print("\nA soma dos numeros é %f!" % soma)
print("\nA media dos numeros é: %f!" % media)

if (media > 6):
    print("Você foi APROVADO!")
else:
    print("REPROVADO seu bosta!")

enter = input("\nPressione <Enter> para encerrar...")

