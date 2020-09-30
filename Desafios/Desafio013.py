"""
Cálculo do salário do funcionário
15% de aumento
"""
salario = float(input('Qual o salário do funcionário: R$ '))
salarioNovo = salario * 115 / 100
print('O novo salário é R$ {:.2f}'.format(salarioNovo))

# ou

novo = salario + (salario * 15 / 100)
print('O novo salário é de R$ {:.2f} reais.'.format(novo))
