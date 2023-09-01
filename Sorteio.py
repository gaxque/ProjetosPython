from random import choice

n1 = str(input('Primeira pessoa: '))
n2 = str(input('Segunda pessoa: '))
n3 = str(input('Terceira pessoa: '))
n4 = str(input('Quarta pessoa: '))
n5 = str(input('Quinta pessoa: '))
lista = [n1, n2, n3, n4, n5]
escolhido = choice(lista)
print('O aluno foi escolhido foi:  {}'.format(escolhido))