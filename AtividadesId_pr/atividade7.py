n1 = int(input('insira o primeiro número '))
n2 = int(input('insira o segundo número '))
n3 = int(input('insira o terceiro número '))

if n1 > n2 and n1 > n3:
    print(n1)
    if n2 > n3:
        print(n2, "\n", n3)
    else:
        print(n3, "\n", n2)

if n2 > n1 and n2 > n3:
    print(n2)
    if n1 > n3:
        print(n1, "\n", n3)
    else:
        print(n3, "\n", n1)

if n3 > n2 and n3 > n1:
    print(n3)
    if n2 > n1:
        print(n2, "\n", n1)
    else:
        print(n1, "\n", n2)