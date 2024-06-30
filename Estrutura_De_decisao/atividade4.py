"""
faca um programa que peca duas cores primarias e imprima a cor resultante da mistura delas, caso alguma das cores que o usuario informar nao for uma cor primaria, notifique-o
"""
print('Digite abaixo duas cores primarias e veja qual a cor secundaria que resulta: ')

cor1 = (input('Digite primeira cor  primaria: '))
cor2 = (input('Digite a segunda cor primaria: '))

if (cor1 == 'azul' and cor2 == 'amarelo') or (cor1 == 'amarelo' and cor2 == 'azul'):
    print(f' A mistura das duas resulta na cor secundaria verde')

elif (cor2 == 'vermelho' and cor1 == 'amarelo') or (cor1 == 'vermelho' and cor2 == 'amarelo'):
    print('A mistura das duas cores resulta na cor secundaria laranja')

elif (cor1 == 'vermelho' and cor2 == 'azul') or (cor1 == 'azul' and cor2 == 'vermelho'):
    print('A mistuta das duas cores secundarias resulta nas cores: roxo e violeta')

else:
    print('Nao e uma cor primaria')
