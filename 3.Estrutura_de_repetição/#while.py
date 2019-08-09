# Contador
i = 1
while i <= 10:
    print("Valor de i: %d" %i)
    i += 1
print("\nFim!")

# Tabuada simples
n = int(input("Informe N: "))
i = 0
while i<= 10:
    print("%d x %d = %d" %(n, i, n*i))
    i += 1

# Laço infinito
soma = 0
while True:
    numero = int(input("Digite o valor pra somar ou 0 para sair: "))
    if numero == 0:
        break
    soma += numero
print("Soma: %d" %soma)