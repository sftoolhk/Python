num = int(input("\nDigite um numero inteiro: "))
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[33m", end = '')
    else:
        print("\033[31m", end = '')
    print("{} ".format(c), end = '')

enter = input("\nPressione <Enter> para encerrar...")
