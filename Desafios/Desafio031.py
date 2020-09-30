"""
Faça um programa que leia uma distância e calcule o valor da passagem sabendo que:
R$ 0.50 por Km até 200 Km
R$ 0.45 por Km acima de 200 Km
"""
menor = 0.50
maior = 0.45
distancia = float(input('Digite a distância total do percurso: '))
print('Você está prestes a começar uma viagem de {} Kilômetros. Boa viagem!'.format(distancia))
if distancia <= 200:
    print('O custo da viagem será de R${:.2f} reais.'.format(distancia * menor))
else:
    print('O custo da viagem será de R${:.2f} reais.'.format(distancia * maior))

#  Outra forma:

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preco))

#  Outra maneira: Mesma linha
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preco))
