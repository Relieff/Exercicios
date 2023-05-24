# lista compostas

pessoas = list()
dados = list()

dados.append('Pedro',21)
pessoas.append(dados[:]) #O simbolo [:] é um fatiamento completo da estrutura( copia dos dados)

print(pessoas)
print(dados)