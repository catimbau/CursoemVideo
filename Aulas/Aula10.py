import random
# tempo = int(input('Quantos anos tem seu carro? '))
tempo = random.randint(1, 10)
print('Seu carro tem {} anos'.format(tempo))
print('Carro novo' if tempo < 6 else 'carro velho')
if tempo < 6:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')


