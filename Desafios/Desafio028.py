"""
Faça um programa que escolhe um número aleatóriamente entre 0 e 5 e o usuário tenta adivinhar.
"""

from random import randint
from time import sleep
sorteio = randint(0, 5)
print('-=-' * 10)
print('Pensarei em um número de 0 a 5! Tente adivinhar!')
print('-=-' * 10)
numero = int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(1)
if numero == sorteio:
    print('Parabéns! Você acertou!!')
else:
    print('Pensei no número {} e você digitou {}. ERROU!!'.format(sorteio, numero))
