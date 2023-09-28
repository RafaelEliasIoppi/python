lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #compara com o utlimo elemento da lista
       lista.append(n) #insere no final da lista
       print(f'adicionado ao final da lista posição {c}')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados{lista}')

