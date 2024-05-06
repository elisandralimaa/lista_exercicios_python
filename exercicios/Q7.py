KmRodados = float(input('Quantos Km percorridos o carro fez? '))
DiasAlugado = int(input('Quantos dias foram alugados? '))
custo = 98.75
adcional = 0.028
PrecoAPagar = (DiasAlugado * custo) + (KmRodados * adcional)
print('O valor a pagar pelos dias de uso do carro alugado é: ', round(PrecoAPagar, 2))