ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar [S/N]: '))
    if resp in 'Nn':
        break
print('-=' * 10)
print(f'{"No.":<4}{"Nome":<10}{"Média":<4}')
print('--' * 10)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:<4}')
while True:
    print('-=' *20)
    opc = int(input('Digite o código do aluno para saber as notas (999 interrompe):  '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'As notas de {ficha[opc][0]} são: {ficha[opc][1]}')
print('Volte sempre')



