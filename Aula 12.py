nome = str(input('Olá, digite seu nome: '))
if nome == 'Átila':
    print('Que nome bonita você tem!')
elif nome == 'Lohany'or 'Fabricio' or 'Juan' or 'Vinicius':
    print('Que nome brabo!')
else:
    print('Seu nome é bem normal...')
print('Tenha um bom dia, {}!'.format(nome))