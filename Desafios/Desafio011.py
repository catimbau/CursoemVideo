# Make a program that reads the width and height of a wall in meters, calculate its area and the amount of
# paint needed to paint it, knowing that each liter of tin paints an area of 2m²

width = float(input('Digite a largura da parede em metros: '))
height = float(input('Digite a altura da parede em metros: '))
total = (width * height) / 2
print('Considerando que a largura da parede tenha {} metros\n'
      'e a altura dela seja de {} metros,\n'
      'então a quantidade de litros de tinta necessária para pintar a parede inteira é de: {}'
      .format(width, height, total))
