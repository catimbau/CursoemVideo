# 29/08/2020
# Aula 07 - Operadores Aritméticos

# + Adição              #5 + 2 == 7
# - Subtração           #5 - 2 == 3
# * Multiplicação       #5 * 2 == 10
# / Divisão             #5 / 2 == 2.5
# ** Potência           #5 ** 2 == 25
# // Divisão inteira    #5 // 2 == 2
# % Resto da divisão    #5 % 2 == 1

# Ordem de Precedência
# 1) ()
# 2) **
# 3) * / // % (O que aparecer primeiro)
# 4) + -

# Exemplo:
# 5 + 3 * 2 => 5 + 6 => 11
# 3 * 5 + 4 ** 2 => 3 * 5 + 16 => 15 + 16 => 31
# 3 * (5 + 4) ** 2 => 3 * 9 ** 2 => 3 * 81 => 243

# Potenciação pode ser calculada como pow(4,2)
# Raíz Quadrada pode ser calculada como 81**(1/2)

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))  # {:=^20} Centraliza e coloca o sinal de igual antes e depois

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
print('A soma vale {},\n a multiplicação vale {}'.format(s, m), end=' ')  # end para permanecer na mesma linha e
# \n para quebrar a linha
print('A divisão é: {}'.format(d))
