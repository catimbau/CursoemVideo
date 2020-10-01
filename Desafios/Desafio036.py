"""
Calcular um empréstimo baseado no valor da casa, salário e quantidade de anos para quitar.
"""
casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o seu salário: R$ '))
anos = int(input('Digite a quantidade de anos inteiros para quitação: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos))
print('A prestação será de R$ {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')
