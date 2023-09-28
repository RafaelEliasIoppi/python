lista = []
for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    if i == 0 or valor > lista[-1]:
        lista.append(valor)
        print(f'Valor adicionado ao fim da lista ... {valor}')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Valor adicionado na posição: ... {pos}')
                break
            pos += 1

print('Lista ordenada: {} '.format(lista))
