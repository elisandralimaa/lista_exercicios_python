altura = float(input('Qual sua altura? '))
nome = input('Qual o seu nome?')
peso = 0
sexo = input('Digite aqui seu sexo: ')

if sexo.lower() == 'homem':
    peso = (72.7 * altura) - 58
    print(f'O peso de {nome} é  {peso}')
elif sexo.lower() == 'mulher':
    peso = (62.1 * altura) - 44.7
    print(f'O peso de {nome} é {peso}')
else:
    print('Não binário')
