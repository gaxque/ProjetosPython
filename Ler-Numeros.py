#Faça um programa que leia três ou mais números e
#mostre qual é o maior e qual é o menor.

v1 = int(input('Digite um numero: '))
v2 = int(input('Digite outro numero: '))
v3 = int(input('Digite mais um numero: '))
v4 = int(input('Por fim, digite o ultimo numero: '))

#MENOR VALOR
menor = v1
if v2 < v1 and v2 < v3 and v2 < v4:
    menor = v2
if v3 < v1 and v3 < v2 and v3 < v4:
    menor = v3
if v4 < v1 and v4 < v2 and v4 < v3:
    menor = v4

#MAIOR VALOR
maior = v1
if v2 > v1 and v2 > v3 and v2 > v4:
    maior = v2
if v3 > v1 and v3 > v2 and v3 > v4:
    maior = v3
if v4 >  v1 and v4 > v2 and v4 > v3:
    maior = v4

print('O maior valor digitado foi {} e o menor valor foi {}'.format(maior, menor))