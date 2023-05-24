coresletras ={'branco': '\033[30m',
              'limpa': '\033[m',
              'vermelho': '\033[31m',
              'verde': '\033[32m',
              'amarelo': '\033[33m',
              'azul': '\033[34m',
              'magenta': '\033[35m',
              'ciano': '\033[36m',
              'cinza': '\033[37m'}
n1 = float(input('{}Digite a primeira nota:{} '.format(coresletras['magenta'], coresletras['limpa'])))
n2 = float(input('{}Digite a segunda nota:{} '.format(coresletras['verde'], coresletras['limpa'])))
m = (n1 + n2)/2
print('Sua média foi {}{:.1f}{}'.format(coresletras['azul'], m, coresletras['limpa']))
if m >= 6:
    print('Sua nota tá boa!')
else:
    print('Sua nota foi pessima')