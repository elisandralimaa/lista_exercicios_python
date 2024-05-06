horas = float(input('Quanto você ganha por hora trabalhada?'))
horasMes = float(input('Quantas horas você trabalha no mês? '))
calculo = horas * horasMes
descontoImpostoDeRenda = (calculo / 100) * 11   # Usando a primeira formula da porcentagem
descontoInss = calculo * 0.08                   # Usando a segunda formula da porcentagem
descontoSindicato = (calculo / 100) * 5         # Usando a primeira formula da porcentagem
salarioLiquido = calculo - (descontoImpostoDeRenda + descontoInss + descontoSindicato)
print('O seu salário bruto é de R${:.2f}\nValor descontado do IR R${:.2f}\nValor descontado do INSS R${:.2f}\nRepasse sindicato R${:.2f}\nValor liquido R${:.2f}'
      .format(calculo,descontoImpostoDeRenda,descontoInss,descontoSindicato, salarioLiquido))
