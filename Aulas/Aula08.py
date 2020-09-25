"""
Utilizando Modulos
24 09 2020
"""
from math import sqrt
import random
# num = int(input('Digite um número: '))
num = random.randint(1, 200)
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, (raiz)))
