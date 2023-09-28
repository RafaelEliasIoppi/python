frase = str(input('Digite uma frase:')).strip().upper() # tira o espaço e joga tudo pra maisucula
palavras = frase.split() # separa em palvras
junto = ''.join(palavras) # junta as palavras com o caracter que esta entre ''
inverso = ''
for letra in range(len(junto) - 1, -1, -1): # começa (len(junto)-1: começa na ultima letra, vai ate -1 ( posciao 0 ou primeira letra)
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('É UM PALÍNDROMO')
else:
    print('NÃO É UM PALÍNDROMO')