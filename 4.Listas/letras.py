for caracter in texto:
    if caracter in 'aeiou':
        vogais = vogais + 1
    else:
        consoantes = consoantes + 1

print "Vogais: %d" %vogais
print "Consoantes: %d" %consoantes
print "Total de letras: %d - %d" %(len(texto), (vogais+consoantes))
