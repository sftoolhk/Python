import random
# constantes
MENOR = 1     # limite inferior (inclusive) de um número sorteado
MAIOR = 100   # limite superior (exclusive) de um número sorteado
TAMANHO_DA_SEQ = 5   # tamanho da sequência sorteada

def main():
    # Programa que sorteia 5 inteiros entre 0 e 99.
    semente = int(input("Digite a semente: "))
    random.seed(semente)   ## inicializa o gerador com a semente

    cont = 0
    while cont < TAMANHO_DA_SEQ:
        sorteio = random.randrange(MENOR, MAIOR)
        cont += 1
        print( 'Sorteio', cont, ':', sorteio )

if __name__ == '__main__':

    main()