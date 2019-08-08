n = int(input ("Digite o número a verificar:"))
q = 0
while 10 ** q < n:
    q = q + 1
i = q
f = 0
nf = ni = n
pi = pf = 0
while i > f:
    pi = int(ni / (10 ** (i-1)))
    pf = nf % 10
    if pi != pf:
        break
    f = f + 1
    i = i - 1
    ni = ni - (pi * (10 ** i ))
    nf = int(nf / 10)
if pi == pf:
    print("%d é palíndromo" % n)
else:
    print("%d não é palíndromo" % n)
