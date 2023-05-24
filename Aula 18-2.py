#Pra criar uma lista composta com mais simpliscidade:
pessoas = [['Pedro',21],['Maria',16],['Claudio',43]] #Uma lista dentro de outra lista

print(pessoas[0][0]) #Dentro de pessoas [0] quero o item [0]
print(pessoas[1][1]) #Dentro de pessoas [1] quero o item [1]
print(pessoas[2][0]) #Dentro de pessoas [2] quero o item [0]
print(pessoas[1]) #Quer a lista [1]
print('-'*40)

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')