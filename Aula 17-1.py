## lanche.append('')        Para adicionar no final da lista
## lanche.insert(0,'')        Para inserir em um determinado lugar
## del lanche[]             Eliminar um determinado ponto
## lanche.pop()             Eliminar o ultimo elemento
##lanche.remove('')         Remover o conteudo

##if 'pizza' in lanche:
    ##lanche.remove('pizza') Se PIZZA estiver em lanche: remover a PIZZA

## lista.sort()     Para organizar os valores
## lista.sort(reverse = True)   Ordenados na ordem reversa

num = [2, 4, 6, 8, 10]
num[2] = 3
num.append(7)
num.sort()
num.insert(2,0)
num.pop()
print(num)

if 4 in num:
    num.remove(4)
