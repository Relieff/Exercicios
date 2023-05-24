        #Odem de Procedência
#1= ()
#2= **
#3= * / // %
#4= + -

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor'))
s = n1 + n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
e = n1 ** n2
rd = n1 % n2
print('A soma é {}; \n A divisão é {}; \n O produto é {}'.format(s , d, m), end='\n')
print('A divisão inteira é {}, \n A potência é {}, \n O resto da divisão é {}'.format(di, e , rd))