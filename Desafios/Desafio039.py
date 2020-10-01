"""
Alistamento Militar

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano do nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Você ainda não tem 18 anos. Faltam {} anos para o alistamento'.format(18 - idade))
    ano = atual + (18 - idade)
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:  # ou else
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    ano = atual - (idade - 18)
    print('Você deveria ter se alistado em {}.'.format(ano))
