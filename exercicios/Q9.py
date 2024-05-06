print('Vamos analisar se você será aprovado para a compra do seu carro: ')
emprestimoBancario = float(input('Qual o valor do carro que você quer comprar?'))
salario = float(input('Quanto você ganha por mês?'))
anos = int(input('Quantos anos de financimanto?'))

if(anos > 5):
    print('Infelizmente seu empréstimo não foi aprovado, o tempo é superior a 5 anos')
else:
    prestacao = emprestimoBancario / (anos * 12)
    maximo = (salario * 30 / 100)
    if(prestacao > maximo):
        print('O valor das prestacoes comprometeu mais de 30% do seu salário')
    else:
        print('O seu emprestimo foi aprovado no valor de R${:.2f} em {} anos a prestacao será de R${:.2f}'
              .format(emprestimoBancario, anos, prestacao))

        print('O seu emprestimo foi aprovado\nEmprestimo: R${:.2f}\nTempo de financiamento: {} anos\nPrestacao: R${:.2f}'
              .format(emprestimoBancario, anos, prestacao))










