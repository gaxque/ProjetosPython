#Exercício 28 – Jogo da Adivinhação v.1.0

from random import randint
computador = randint(0, 3) #Faz o computador pensar

print ('-=-' * 20)
print ('Vou pensar em um nuemro entre 0 e 3, tente advinhar...')
print ('-=-' * 20)

jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('Parabéns você acertou!')
else: 
    print('Errou eu pensei no número: {} e não no número: {}' .format(computador, jogador))
