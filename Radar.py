#Exercício 29 – Radar eletrônico

velocidade = float(input('Qual a velocidade atual? '))

if velocidade > 60:
    multa = (velocidade-60) * 7
    print('Você está acima da velocidade e sua multa será de: R${:.2f}' .format(multa))
else:
    print ('Você está dentro da velocidade permitida - Dirija com cuidado')