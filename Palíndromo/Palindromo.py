frase = str(input('\nDigite algo: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
espelho = juntar[::-1]
print('\nO inverso de {} é {}'.format(juntar, espelho))
if espelho == juntar:
    print('\nPalíndromo!')
else:
    print('\nOnly words!')
