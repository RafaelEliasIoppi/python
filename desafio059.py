from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Qual o maior
    [4] Novos números
    [5] Sair do progama''')
    opcao = int(input('>>>>>>>> Escolha sua opção: '))
    if opcao == 1:
       soma = n1 + n2
       print('--=--' *7)
       print('A soma de {} + {} = {}\n'.format(n1, n2, soma))
       print('--=--'*7)
    elif opcao == 2:
        multi = n1 * n2
        print('--=--' *7)
        print('A multiplicação de {} X {} = {}'.format(n1, n2, multi))
        print('--=--' *7)
    elif opcao == 3:
         if n1 > n2:
            print('--=--' *7)
            print('{} é maior que {}'.format(n1, n2))
            print('--=--' *7)
         elif n2 > n1:
             print('--=--' *7)
             print('{} é maior que {}'.format(n2, n1))
             print('--=--' *7)
         elif n1 == n2:
             print('--=--' *7)
             print('{} é igual a {}'.format(n1, n2))
             print('--=--' *7)
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor:  '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Fim do Programa')
    else:
        print('--=--' *7)
        print('Opçao inválida! Digite novamente.')
        print('--=--' *7)
    sleep(2)