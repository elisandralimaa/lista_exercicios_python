n = int(input('Digite um número '))
numerosPrimos = []
divisores = 0
qtdDivisoes = 0
for i in range(1, n + 1):
    for j in range(2,i):
        if i % j == 0:
            divisores += 1
            break
        qtdDivisoes += 1
    if divisores == 0:
        numerosPrimos.append(i)
    divisores = 0


print(numerosPrimos)

print(f"Foram realizadas {qtdDivisoes} divisoes")