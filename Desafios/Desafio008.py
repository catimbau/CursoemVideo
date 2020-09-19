# Write a program that reads a value in meters and displays it converted to centimeters and millimeters

n1 = float(input('Digite o valor em metros: '))
centimetros = n1 * 100
milimetros = n1 * 1000
print('O número em metros é: {},\n'
      'O número em centímetros é: {}, \n'
      'O número em milímetros é: {}'
      .format(n1, centimetros, milimetros))
