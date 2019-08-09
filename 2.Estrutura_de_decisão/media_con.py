# Programa media com resultado da nota

print('\n')
nota1 = float(input("Entre com a primeira nota"'\n'))
nota2 = float(input("Entre com a segunda nota"'\n'))
media = (nota1 + nota2) / 2

if (media <= 4):
    print("Sua nota foi ", media, "e você foi aprovado com conceito E e REPROVADO")
elif (media > 4 and media <= 6):
    print("Sua nota foi", media, "e você foi aprovado com conceito D e REPROVADO")
elif (media >= 6 and media < 7.5):
    print("Sua nota foi", media, "e você foi aprovado com conceito C e APROVADO")
elif (media >= 7.5 and media < 9):
    print("Sua nota foi", media, "e você foi aprovado com conceito B e APROVADO")
else:
    print("Sua nota foi", media, "e você foi aprovado com conceito A e APROVADO")

enter = input("\nPressione <Enter> para encerrar...")    
