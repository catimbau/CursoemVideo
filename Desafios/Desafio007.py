# Develop a program that reads a student's two grades, calculates and displays the average

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A primeira nota foi: {},\n'
      'a segunda nota foi: {}\n'
      'e a média é: {}'.format(n1, n2, media))
