# Create an algorithm that reads a number and shows its double, triple and square roots

n1 = int(input('Digite um número inteiro: '))
do = n1 * 2
tr = n1 * 3
raiz = n1**(1/2)

print('O número digitado foi {}, '
      'seu dobro é {}, '
      'seu triplo é {} '
      'e sua raíz quadrada é {}'
      .format(n1, do, tr, raiz))

# or

print('O número digitado foi {}, '
      'seu dobro é {}, '
      'seu triplo é {} '
      'e sua raíz quadrada é {}'
      .format(n1, n1*2, n1*3, n1**(1/2)))
