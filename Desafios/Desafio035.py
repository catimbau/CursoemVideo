"""
Verificar se as três segmentos de retas podem formar um triângulo.
"""
print('-=-' * 8)
print('Analisador de Triângulos')
print('-=-' * 8)
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a primeira reta: '))
r3 = float(input('Digite a primeira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar triângulo!')
else:
    print('Os segmentos acima NÃO formam triângulo!')
