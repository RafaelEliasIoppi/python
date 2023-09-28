from random import randint
lista = [(randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), randint(0, 10), (randint(0, 10)),
         (randint(0, 10)), (randint(0, 10))]
print(f'Lista Desordenada: {lista}')
cont = 0
tamanho = len(lista)
while cont < tamanho:
    for pos in range(tamanho - 1):
        if lista[pos] >= lista[pos+1]:
             temp = lista[pos+1]
             lista[pos+1] = lista[pos]
             lista[pos] = temp
    cont += 1
print('--' *23)
print(f'Lista ordenada:    {lista}')
print('--'*23)



