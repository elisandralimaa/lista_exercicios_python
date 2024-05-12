# Escreva um algoritimo que leia uma variavel numero e
# itere ate o numero lido escreva a seguinte mensagem para os numeros pares utilizando o 'for':
# Ex1: O numero 1 eh par
# Ex2: O numero 2 eh par
"""num = int(input('Digite um numero'))

for par in range(0, num, 2):
    print(f'O {par} é par ')"""

num = int(input('Digite um numero '))

for recebe in range(0, num + 1):
    if recebe % 2 == 0:
        print(f' o {recebe} é par ')
