"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

letra = input('Digite M - Masculino ou F - Feminino: ')

if letra.upper() == 'F':
    print('Feminino')
elif letra.upper() == 'M':
    print('Masculino')

else:
    print('Sexo Invalido')

