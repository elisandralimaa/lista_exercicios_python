print ('coloque aqui os lados do seu triangulo ')
lado1 = float(input('Qual o lado 1 do triangulo? '))
lado2 = float(input('Qual o lado 2 do triangulo? '))
lado3 = float(input('Qual o lado 3 do triangulo? '))

if  (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1):
    print(' Não é um trinagulo')
elif (lado1 == lado2) and (lado1 == lado3):
        print('Trainagulo Equilatero')
elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print('Triângulo Isósceles')
else:
    print('Triângulo Escaleno')



