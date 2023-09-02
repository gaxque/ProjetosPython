# Escreva um programa para aprovar o empréstimo bancário para a
# compra de uma casa. Pergunte o valor da casa, o salário do 
# comprador e em quantos anos ele vai pagar. A prestação mensal não 
# pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep

casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / ( anos * 12 ) 
minimo = ( salario * 30 / 100)

print(' [ Consultando com o banco... ]')
sleep(2)

if prestacao <= minimo:
    print('\033[1;32;40m [ Olha, só o banco APROVOU!! ]  \033[m')
    sleep(3)
    print('\033[1;32;40m [ Aguarde um momento... ]  \033[m')
    sleep(2)
    print('Para pagar uma casa de \033[1;32;40mR$ {:.2f}!\033[m em {} anos'.format(casa, anos))
    print('A prestação será de: \033[1;32;40mR$ {:.2f}!\033[m '.format(prestacao))

else:
    print ('#\033[1;31;40m[Infelizmente o Banco não aprova esse financiamento. Pois seu salário está abaixo de 30%]\033[m')
    sleep(2)




#Colocar cor, treinado até nao esquecer!!!!!
#     [ \033[1;32;40m ] Começo   [ !\033[m ] Final 