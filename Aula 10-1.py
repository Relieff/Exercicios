coresletras = {'limpa': '\033[m',
               'azul': '\033[34m',
               'amarelo': '\033[33m',
               'vermelho': '\333[31m',
               'verde': '\033[32m',
               'magenta': '\033[35m',
               'ciano': '\033[36m',
               'cinza': '\033[37m',
               'pretoebranco': '\033[7,30m'}
coresbg = {'branco': '\033[107m',
            'vermelho': '\033[41m',
            'verde' : '\033[42m,',
            'amarelo' : '\033[43m',
            'azul': '\033[44m',
            'magenta': '\033[45m',
            'ciano' : '\033[46m',
            'limpa': '\033[m',
            'cinza':'\033[47m'}


tempo = int(input('{}Quantos anos tem seu carro:{} '.format(coresletras['azul'], coresletras['limpa'])))
if tempo <= 3:
    print('{}Carro novo naquele jeito {}'.format(coresletras['verde'], coresletras['limpa']))
else:
    print('{}Carro velho e fudido{}'.format(coresletras['vermelho'], coresletras['limpa']))
print('------Fim------')
