mulheres = homens = jovens = maiores = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Informe seu sexo [M]/[F]: ')).strip().upper()[0]
    escolha = str(input('Deseja continuar [S]/[N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        mulheres += 1
    if sexo == 'F' and idade < 20:
        jovens += 1
    if idade > 18:
        maiores += 1
print('Há {} com mais de 18 anos'.format(maiores))
print('Há {} mulheres com menos de 20 anos'.format(jovens))
print('Há {} homens no total'.format(homens))

