#Aula 10 – Condições (Parte 1)

# nome = str(input('Qual é seu nome: '))
# if nome == 'Gabriel':
#    print('Que nome bonito! ')
# print('Olá, {} '.format(nome))

n1 = float(input('Digite a primeira nota: ')) 
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

m = (n1 + n2 + n3 + n4 ) / 4

print('A sua média foi {:.1f}'.format(m))

if m>= 6.0:
    print('Sua nota está acima da média!')
else:
    print('Sua nota está abaixo da média!')

#IF SIMPLIFICADO>    
#print("FRASE ACIMA DA MEDIA" if m>=6.0 else "FRASE ABAIXO DA MEDIA")