nota1 = float(input('Digite aqui sua primeira nota'))
nota2 = float(input('Digite aqui sua segunda nota'))
media = (nota1 + nota2) / 2

if(media >= 6):
    print('Está aprovado!')
elif(media >= 1 and media < 6):
    print('Está de recuperação, você precisa de pelo menos', 12 - media, 'para passar')
else:
    print('Reprovado')

