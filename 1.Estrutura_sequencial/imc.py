# Calculo de Indice de Massa corporea ideal para Homem e Mulher
#M <> m == V # masculino
#F <> f == F # feminino
altura = float(input("Entre com a sua altura: "))
sexo = input("Entre com o seu sexo: ")

if (sexo.upper() == 'M'):
    imc = (72.7 * altura) - 58
elif (sexo.upper() == 'F'):
    imc = (62.1 * altura) - 44.7

print("\nSeu peso ideal e %s" % imc)

enter = print("\nPressione <Enter> para encerrar...")
