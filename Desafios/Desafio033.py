"""
Digite 3 números inteiros e mostre a ordem de grandeza deles.
"""
#  for i in i < 3:
#    int(input('Digite o {} número: '.format(i)))


a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor é: {}'.format(menor))
print('O maior foi: {}'.format(maior))
