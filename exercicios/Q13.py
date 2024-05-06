litros = float(input('Digite quantos litros você quer abastecer? '))
combustivel = input('Digite A para álcool ou G para gasolina: ')
preco = 0
if combustivel == 'A' or combustivel == 'a':
    preco = litros * 4.498
    if litros <= 20:
        preco -= 4.498 * litros * 3 /100
    else:
        preco -= 4.498 * litros * 5 / 100
    print(f'O valor a pagar de A-lcool é R${preco:.2f}')

elif combustivel == 'G' or combustivel == 'g':
       preco = litros * 5.759
       if litros <= 20:
           preco -= 5.759 * litros * 4 / 100
       else:
           preco -= 5.759 * litros * 6 / 100

       print(f'O preço a pagar de G-gasolina é R${preco:.2f}')

#valor = 0
#valor += 10   # valor = valor + 10
#valor -= 5    # valor = valor - 5
#valor /= 10   # valor = valor /10
