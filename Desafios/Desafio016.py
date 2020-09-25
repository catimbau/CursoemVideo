"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
Ex: Digite um número: 6.127
O número 6.127 tem a parte Inteira 6.
"""
# import math
from math import trunc
import random
outro = random.uniform(1, 1000)
# num = float(input('Digite um número qualquer: '))
# print('O número {} tem a parte Inteira {}'.format(num, int(math.floor(num))))
print('O número {:.3f} tem a parte Inteira {}'.format(outro, int(trunc(outro))))

"""
Versão da aula:

Método 1)
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

Método 2) Sem importar função externa
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

"""