"""
Faça um programa que leia a velocidade do carro inserida pelo usuário e calcule se está acima da velocidade de 80km/h
e se estiver, calcule o valor da multa sendo que o cálculo é de R$ 7,00 para cada Km/h acima do limite
"""

valor_multa = 7
vel_max = 80
vel = float(input('Digite a velocidade do carro: '))
if vel <= vel_max:
    print('Você está dentro do limite de velocidade.')
else:
    diferenca = vel - vel_max
    print('\033[1;31mVocê estava acima da velocidade permitida em {:.2f} Km/h e sua multa é de R${:.2f} reais\033[m'
          .format(diferenca, valor_multa * diferenca))
print('Tenha um bom dia! Dirija com segurança!')
