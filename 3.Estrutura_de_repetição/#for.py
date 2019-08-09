for i in range(5):
    print(i)
    ou
    print(i, end = ' ') # definir como será a saída

# %s = string
# %d = inteiro
____________________________________________________

for i in range(10, 21, 2):
    print(i, end = ' ')
____________________________________________________

a = 0
b = 10
for i in range(b, a, -1):
    print(i, end = ' ')
____________________________________________________

nomes = ['Ana', 'Zé', 'Maria', 'Ana', 'José']
for nome in nomes:
    print(nome)
____________________________________________________

carros = ['Fusca', 'Ferrari', 'Camaro', 'Gol']
for carro in carros:
    print("%s: %d" %(carro, len(carro)))
____________________________________________________

notas = [10, 7, 5, 5, 7, 9]
for nota in notas
    if nota < 6:
        continue
    print("Nota: %d" % nota)
____________________________________________________

#Estrutura de repetição e compreensão de lista
quadrados = []
for i in range (1, 11):
    quadrados.append(i * i)
print(quadrados)
____________________________________________________
quadrados = [i * i for i in range(1, 11)]
print(quadrados)
____________________________________________________
quadrados = [i * i for i in range(1, 11)]
print(quadrados)