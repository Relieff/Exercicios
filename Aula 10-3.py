coresletras = {'branco': '\033[30m',
               'vermelho': '\033[31m',
               'verde': '\033[32m',
               'amarelo': '\033[33m',
               'azul': '\033[34m',
               'magenta':'\033[35m',
               'ciano': '\033[36m',
               'cinza': '\033[37m',
               'limpa': '\033[m'}
nome = str(input('{}Digite seu nome {}'.format(coresletras['amarelo'], coresletras['limpa'])))
if nome == 'Gustavo':
    print('{}Que{} nome{} lindo{} você{} tem!{}'.format(coresletras['vermelho'], coresletras['verde'],coresletras['azul'], coresletras['cinza'],coresletras['branco'],coresletras['ciano'],coresletras['limpa']))
else:
    print('{}Nome feio pra caralho!{}'.format(coresletras['vermelho'], coresletras['limpa']))
print('Bom dia {}{}{}, filho da puta'.format(coresletras['magenta'], nome, coresletras['limpa']))

