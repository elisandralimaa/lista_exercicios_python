num = int(input("digite aqui um número inteiro: "))
listaNumerosDivisivel = [1, num]

for valor in range(2, num):
    if ((num % valor) == 0):
        listaNumerosDivisivel.append(valor)
else:
    if (len(listaNumerosDivisivel) > 2):
        frase = "Ele nao eh primo.\nAqui estao os numeros divisiveis: "
        for divisivel in listaNumerosDivisivel:
            frase += str(divisivel) + ", "
        print(frase)
    else:
        print("Ele é primo")