nome = str(input('Digite seu nome completo: ')).strip()# strip tira os espaços antes e depois
lista = nome.split()
print('Seu primeiro nome é: {}'.format(lista[0]))
print('O último nome é: {}'.format(lista[len(lista)-1]))