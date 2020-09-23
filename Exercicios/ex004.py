# Dissecando uma variável

n1 = input('Digite algo: ')
print('O tipo primitivo é ', type(n1))
print('É Alfanumérico? ', n1.isalnum())
print('É alfabético? ', n1.isalpha())
print('É numérico? ', n1.isnumeric())
print('Somente espaços? ', n1.isspace())
