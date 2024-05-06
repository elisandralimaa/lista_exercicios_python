velocidade = float(input('Qual velocidade percorrida do carro ? '))
if( velocidade > 60):
    print('MULTADO! você excedeu o limite permitido que é 60KM/h')

    if(velocidade <= 80):
        multa = (velocidade - 60) * 7
        print( f'você deve pagar uma multa de R${multa:.2f}.')

    elif(velocidade <= 100):
       multa = (velocidade - 60) * 14
       print(f'você deve pagar uma multa de R${multa:.2f}.')

    else:
      multa = (velocidade - 60) * 39
      print(f'você deve pagar uma multa de R${multa:.2f}.')

else:
    print('Não ultrapasse a velocidade, repeite os limites de velocidade')

