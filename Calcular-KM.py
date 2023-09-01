#Calculando o preço da viagem para 0.50 até 200km se passar disso 0.45

num = int(input('Digite a distância: '))
if num <= 200:
    distancia = num * 0.50
    print('Nessa distância, ficará por: R$ {:.2f}'.format(distancia))
else:
    distancia2 = num * 0.45
    print('Nessa distância, ficará por: R$ {:.2f}'.format(distancia2))



#Da pra fazer o IF/ELSE assim também: 
#    num=distancia*0.50 if distancia <= 200 else distancia * 0.45 
#gostei nao mas é isso ai gabriel do futuro, ta anotado.
