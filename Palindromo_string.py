#Abrir o arquivo
f = open('pt-BR-utf8', 'r')

#ler uma linha
for line in f:
    palavra = line.replace("\n", "")
    palavra = palavra.lower()
    #inverter a palavra
    palavra_reversa = palavra[::-1]

    #comparar se igual, printar
    if len(palavra) == 1:
        continue
    elif palavra == palavra_reversa:
        print(palavra)
