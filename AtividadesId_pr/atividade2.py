import datetime

def try_convert_to_date(data):
    try:
        data_tipo = datetime.datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        data_tipo = None
    return data_tipo

data = input('Digite aqui a data de hoje no formato dd/mm/aaaa ')
data_tipo = try_convert_to_date(data)

if data_tipo != None:
    print('Data válida')
else:
    print('Data inválida')

