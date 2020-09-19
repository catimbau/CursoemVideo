#Aula 06 em 29/08/2020
#Curso de Python 3 - Mundo 1: Fundamentos
#Primitives Types and Data Output
#Ler dois números e calcular a soma

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))
soma = (n1 + n2)
print('A soma dos dois números é: ', soma)

#Tipos Primitivos
#int 7 -4 0 9875
#float 4.5 0.076 -15.223 7.0
#bool True False
#str "Olá" "7.5"

#print('A soma vale', s)
#print('A soma vale()'.format(s))

print(type(soma))
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))

#Leia algo e mostre se é de algum tipo específico
n3 = input('Digite algo: ')
print('Alfanumérico?', n3.isalnum())
print('Letras? ', n3.isalpha())
print('Espaço?' , n3.isspace())
