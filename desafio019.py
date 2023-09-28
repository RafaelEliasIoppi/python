from random import choice
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digte o quarto nome: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))
