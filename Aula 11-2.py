coresletras = {'limpa': '\033[m',
               'azul': '\033[34m',
               'amarelo': '\033[33m',
               'vermelho': '\333[31m',
               'pretoebranco': '\033[7;30m'}
coresbg = {'branco': '\033[107m',
            'vermelho': '\033[41m',
            'verde' : '\033[42m,',
            'amarelo' : '\033[43m',
            'azul': '\033[44m',
            'magenta': '\033[45m',
            'ciano' : '\033[46m',
            'limpa': '\033[m',
            'cinza':'\033[47m'}
nome = str(input('Qual seu nome?'))
print('Olá, seja bem vindo {}{}{}, prazer em te conhecer'.format(coresletras['amarelo'], coresbg['branco'], nome , coresletras['limpa'], coresbg['limpa']))
