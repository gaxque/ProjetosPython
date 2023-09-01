#Par ou Impar?

num = int(input("Digite um número: "))
res = num % 2 #Vai me dar o resultado 1 ou 0 para eu usar o <IF>
if res == 0:
    print('O número {} é PAR'.format(num))
else: 
    print('O número {} é IMPAR'.format(num))
