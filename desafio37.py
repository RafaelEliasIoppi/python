n1 = int(input('Digite um número inteiro: '))
print(''' Escolha a opção desejada:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL 
[ 3 ] Converter para HEXADECIMAL ''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print('O número {} em binário é: {}'.format(n1, bin(n1)))
elif opcao == 2:
    print('O número {} em octal é: {}'.format(n1, oct(n1)))
elif opcao == 3:
    print(' O número {} em Hexadecimal é: {}'.format(n1, hex(n1)))
else:
    print('Opcao Inválida')