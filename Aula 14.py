par = impar = 0
n = 1

while n != 0:
    n = int(input('Digite um valor: '))
    
    if n % 2 == 0:
        par += 1
    
    else:
        impar += 1
print('Os numeros pares são {} e os impares são {}'.format(par, impar))
print('Acabou')