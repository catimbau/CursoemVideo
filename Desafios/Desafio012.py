"""
Cálculo de desconto em produtos
Desconto de 5%
"""
preco = float(input('Digite o preço do produto: R$ '))
desconto = preco - (preco * 5 / 100)
print('O preço do produto com desconto ficou R$ {:.2f} reais.'.format(desconto))

# Outra forma:
preco = preco * 95 / 100
print('Novo preço: R$ {:.2f} reais.'.format(preco))
