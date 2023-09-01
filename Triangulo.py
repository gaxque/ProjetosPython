# Desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem 
# ou não formar um triângulo.

from time import sleep 
print('-='*20)
print('\033[1;36;40m ANALISANDO TRIÂNGULOS \033[m ')
print('-='*20)

r1 = float(input('Primeria reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

print('Deixa eu ver...')
sleep(3)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('\033[1;32;40mSim, podem formar um triângulo!\033[m ')
else:
    print ('\033[1;31;40mNão, não podem formar um triângulo!\033[m ')