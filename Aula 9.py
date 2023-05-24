# frase.count('' , )     mostra quantas vezes tem uma determinada letra
# frase.find('')         mostra onde começou uma determinada palavra
# Quando você colocar uma string que não existe na frase o valor será -1
# palavra  in  frase        mostra se uma palavra existe ou não(True or False)
# frase.replace('' , '')    Troca uma string por outra
# frase.upper()       Escreve tudo em capslock
# frase.lower()       escreve tudo em minusculo
# frase.captalize()   Coloca tudo pra minusculo exceto a primeira letra da string
# frase.title()       Analise quantas palavras tem e usa o captalize de forma mais eficiente
# frase.strip()       Remove os espaços inuteis do inicio e o final da string
# frase.rstrip()      Remeve somente os espaços inuteis a direita
# frase.lstrip()      Remeve somente os espaços inuteis a direita
# frase.split()       Separa a string em lista(Por padrão e configurada pelo espaço)
# Se quiser escrever alguma string grande ee usar o print, basta usar 3 vezes aspas('' '' '')
                        #---------------------------

frase = '  Meu cú alargadasso   '
print(frase[0:11])
print(frase.upper())
print(frase.lower())
print(frase.split())
print(frase.count('a'))
print(len(frase.strip()))
print(frase)
print(frase.strip())
print(frase.replace('Meu', 'Seu'))