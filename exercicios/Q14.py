print('Loja de tintas da Eli')
tamanho = float(input('Qual o tamanho em metros quadrado da área a ser pintada? '))
litro = tamanho / 6
latas_18_litros = int(litro / 18)

if litro % 18 != 0:
    latas_18_litros += 1

preco_latas_18_litros = latas_18_litros * 80
galoes_3_6_litros = int(litro / 3.6)

if litro % 3.6 != 0:
    preco_galoes_3_6_litros = galoes_3_6_litros * 25

# Calcula a mistura de latas e galões para minimizar o desperdício
litros_restantes = litro - (latas_18_litros * 18)
latas_mistura = int(litros_restantes / 18)
galoes_mistura = int(litros_restantes - (latas_mistura *18)) / 3.6
if litros_restantes - (latas_mistura * 18) % 3.6 != 0:
    galoes_mistura += 1
preco_mistura = (latas_mistura * 80) + (galoes_mistura * 25)
print(f"Quantidade de latas de 18 litros necessárias: {latas_18_litros}")
print(f"Preço total das latas de 18 litros: R${preco_latas_18_litros:.2f}")

print(f"Quantidade de galões de 3,6 litros necessários: {galoes_3_6_litros}")
print(f"Preço total dos galões de 3,6 litros: R${preco_galoes_3_6_litros:.2f}")

print(f"Mistura de latas e galões:")
print(f"   Latas de 18 litros: {latas_mistura}")
print(f"   Galões de 3,6 litros: {galoes_mistura}")
print(f"Preço total da mistura: R${preco_mistura:.2f}")


