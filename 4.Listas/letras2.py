import random
def jogo():

   vogais = ['a','e','i','o','u']

   letra = random.randint(0,4)
   return vogais[letra]

if __name__=='__main__':
   print jogo()