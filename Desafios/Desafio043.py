"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
"""
altura = float(input('Digite sua altura (m): '))
peso = float(input('Digite seu peso em Kg: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    resultado = 'Abaixo do Peso!'
elif imc < 25:
    resultado = 'Peso Ideal!'
elif imc < 30:
    resultado = 'Sobrepeso!'
elif imc < 40:
    resultado = 'Obesidade!'
else:
    resultado = 'Obesidade Mórbida!'
print('O seu IMC é de {:.1f} e seu status é {}'.format(imc, resultado))
