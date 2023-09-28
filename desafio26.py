frase = str(input('Digite uma frase: ')) # Pode ser o.lower aqui em cima
print('A letra A aparece {} X nesta frase'.format(frase.lower().count('a')))
print('A primeira letra A apareceu na poscição: {}'.format(frase.lower().find('a')+1))
print('A última letra A aparece na posição: {}'.format(frase.lower().rfind('a')+1))