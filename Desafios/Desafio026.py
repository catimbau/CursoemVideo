"""
Quantas vezes aparece a letra 'A' na frase
Em que posição aparece a letra 'A' pela primeira vez
Em que posição aparece a letra 'A' pela última vez
"""

frase = str(input('Digite a sua frase: ')).strip().lower()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('a')+1))
