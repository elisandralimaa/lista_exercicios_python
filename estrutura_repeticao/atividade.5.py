#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
nome = input('Coloque aqui o seu nome: ')
senha = input('Digite sua senha: ')

#forma de validar se senha possui letra e numeros e não é igual ao nome
while senha == nome or (not senha.isalpha() and senha.isnumeric()) or (senha.isalpha() and not senha.isnumeric()):
    print('ERRO: você não pode usar o seu nome como senha')

    senha = (input('Senha: '))