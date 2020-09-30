"""
Faça um programa que leia um número e informe se é PAR ou ÍMPAR!
"""
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('o número {} é \033[1;33mPAR!\033[m'.format(numero))
else:
    print('O número {} é \033[1;36mÍMPAR!\033[m'.format(numero))
