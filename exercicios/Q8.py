import math

catetoOposto = float(input('Qual o comprimento do cateto Oposto? '))
catetoAdjacente = float(input('Qual o comprimento do cateto Adjacente? '))
hipotenusa = math.sqrt(math.pow(catetoOposto, 2) + math.pow(catetoAdjacente, 2))
seno = round(catetoOposto / hipotenusa, 2)
coseno = round(catetoAdjacente / hipotenusa, 2)
tangente = round(catetoOposto / catetoAdjacente, 2)
print('O valor da hipotenusa é', round(hipotenusa, 2))
print('O valor do seno é ', seno)
print('O valor do coseno é ', coseno)
print(' E ainda por cima tenho o valor da tangente ', tangente)



