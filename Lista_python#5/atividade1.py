num = int(input("digite aqui um número inteiro: "))

for primo in range(2,num):
    if ((num % primo) == 0):
        print('Ele não é primo ')
        break

else:
    print("Ele  é primo ")


