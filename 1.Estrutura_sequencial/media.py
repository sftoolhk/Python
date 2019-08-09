# Calculo de media

print('\n')
nota1 = float(input("Entre com a primeira nota "'\n'))
nota2 = float(input("Entre com a segunda nota "'\n'))
nota3 = float(input("Entre com a terceira nota "'\n'))
nota4 = float(input("Entre com a quarta nota "'\n'))
media = float(nota1 + nota2 + nota3 + nota4) / 4
print("\nSua média foi %f!" % media)

if (media > 6):
    print("Você foi APROVADO!")
else:
    print("REPROVADO seu bosta!")

enter = input("\nPressione <Enter> para encerrar...")

