"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para
controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de
peixes maior que o estabelecido pelo regulamento de pesca do estado de São
Paulo (50 quilos) deve pagar uma multa de R$ 4.00 por quilo excedente. João
precisa que você faça um programa que leia a variável peso (peso de peixes) e
calcule o excesso. Gravar na variável excesso a quantidade de quilos além do
limite e na variável multa o valor da multa que João deverá pagar. Imprima os
dados do programa com as mensagens adequadas."""

variavelPeso = float(input('Qantos kg você trouxe? '))
regulamento = 50
excesso = variavelPeso - regulamento
multa = excesso * 4

if variavelPeso == regulamento:
    print('Você está dentro do regulamento')
else:
    print(f'Você trouxe {excesso:.2f} kg de excesso\nPagará de multa R${multa:.2f}')









