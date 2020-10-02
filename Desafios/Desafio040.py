"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
"""
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, sua média foi de \033[1;36m{:.1f}\033[m.'.format(n1, n2, media))
if media < 5:
    situacao = 'REPROVADO!'
elif 5 <= media < 7:
    situacao = 'RECUPERAÇÃO!'
else:
    situacao = '\033[1;36mAPROVADO! PARABÉNS!!\033[m'
print('O status do aluno é: {}'.format(situacao))
