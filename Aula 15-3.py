n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}') #Desse jeito é a 'F string' pode ser substituida pela format. Basta colocar um f mínusculo
#Antes das aspas