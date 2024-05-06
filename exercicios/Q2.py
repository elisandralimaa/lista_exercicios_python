largura = float(input('Qual o valor da largura?'))
altura = float(input('Qual a altura?'))
area = largura * altura
QuantidadeDeTinta = area / 2

print("A quantidade de tinta para pintar a parede é:", round(QuantidadeDeTinta, 2), 'L')