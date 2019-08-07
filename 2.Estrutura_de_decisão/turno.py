print("\nDigite M - matutino, V - vespertino, N - noturno")
turno = input("\nEm que turno você estuda: ")

if (turno.upper() == 'M'):
    print("\nBom Dia!")
elif  (turno.upper() == 'V'):
    print("\nBom Tarde!")
elif  (turno.upper() == 'N'):
    print("\nBom Noite!")
else:
    print("Valor Inválido!")

enter = input("\nPressione <Enter> para encerrar...")