"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
"""
print('\n', '{:=^30}'.format(' LOJAS CATIM '))
preco = float(input('\nDigite o preço do produto: R$ '))
condicao = int(input('''Digite a condição de pagamento conforme abaixo:
[ 1 ] À vista ou cheque
[ 2 ] À vista no cartão
[ 3 ] Até 2x no cartão
[ 4 ] 3x ou mais no cartão.
\nCondição: '''))
if condicao == 1:
    preco: float = preco * (90 / 100)
elif condicao == 2:
    preco: float = preco * (95 / 100)
elif condicao == 3:
    preco: float = preco
    parcela = preco / 2
    print('Sua compra será parcelada em 2x de {:.2f}'.format(parcela))
elif condicao == 4:
    preco: float = preco * (120 / 100)
    totparc = int(input('Quantas pacelas? '))
    parcela = preco / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totparc, parcela))
else:
    print('Digite uma opção válida!')
    quit()
print('O preço total do produto é R$ {:.2f}.'.format(float(preco)))
