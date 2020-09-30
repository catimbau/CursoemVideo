"""
Cálculo do salário de funcionários
Salário acima de R$ 1.250,00 aumento de 10%
Para os inferiores ou iguais, aumento de 15%
"""
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))
