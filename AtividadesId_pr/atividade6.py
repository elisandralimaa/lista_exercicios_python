import math

a = int(input('Qual o valor de a: '))
if a == 0:
  print('Essa equacão não é do 2° grau: ')
else:
   b = int(input('Qual o valor de b '))
   c = int(input('Qual o valor de c '))

   #calculo do delta
   delta = b*b - 4 * a * c

   if delta < 0:
      print('A equacao nao poussui raizes reais. ')
   elif delta == 0:
      raiz = (-b) / (2 * a)
      print(f"Delta é zero. A raiz é {raiz}")
   else:
      raiz1 = (-b + (delta ** (1 / 2))) / (2 * a)
      raiz2 = (-b - (delta ** (1 / 2))) / (2 * a)

      print(f"Delta maior que zero. A raíz 1 é {raiz1:.2f}, e a raiz 2 é {raiz2:.2f}")



