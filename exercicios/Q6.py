preco_produto = float(input('Coloque aqui o preco do seu produto: '))
precoReal = preco_produto * 5.23
taxaFlorida = 6
precoComTaxa =  round((precoReal / 100) * taxaFlorida, 2)
print('$', precoComTaxa)
