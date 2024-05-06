n1 = int(input('Digite um valor '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},\n o produto é {} \ne a divisão é {:.3f}' .format(s, m, d), end='')
print('\nDivisão inteira {} \ne potência {}' .format(di, e))
