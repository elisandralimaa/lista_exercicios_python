turno = input('Qual turno você estuda? Digite M para matutino V vespertino ou N noturno ')

if turno.lower() == 'm' or turno.lower() == 'matutino':
    print('Bom dia')

elif turno.lower() == 'v' or turno.lower() == 'vespertino':
    print('Boa tarde')

elif turno.lower() == 'n' or turno.lower() == 'noturno':
    print('Boa noite')

else:
    print('Valor inválido')
