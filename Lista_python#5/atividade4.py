num = int(input('Digite um número inteiro '))
fatorial = num
for i in range(num -1, 1, -1):
    fatorial *= i            # fatorial = fatorial * i

print(f'O fatoria de {num} é {fatorial}')