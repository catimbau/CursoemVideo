# Create a program that reads how much money (Brazilian Real) a person has in their wallet
# and shows how many dollars they can buy ( U$$1,00 = R$3,27)

real = float(input('Quantos reais você tem na carteira? '))
dolar = real / 3.27
print('Você tem {} reais e seu equivalente em dólares é {}'.format(real, dolar))
