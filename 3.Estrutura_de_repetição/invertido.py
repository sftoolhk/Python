numeros = str(input('\nDigite uma sequncia de numeros: '))
espelho = numeros[::-1]
print('\nO inverso de {} é {}'.format(numeros, espelho))
if espelho == numeros:
    print('\nPalíndromo!')
else:
    print('\nOnly numbers!')

    enter = input("\nPressione <Enter> para encerrar...")
