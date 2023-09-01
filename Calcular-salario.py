#  Escreva um programa que pergunte o salário de um funcionário e 
#  calcule o valor do seu aumento. Para salários superiores
#  a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

#LENDO O SALARIO
salario = float(input('Qual o salario do funcionario? R$ '))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print('Quem ganhava \033[1;37;43mR${:.2f}\033[m passa a ganhar \033[1;37;42mR${:.2f}\033[m agora!' .format(salario, novo))

