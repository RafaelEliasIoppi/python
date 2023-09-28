somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('--------- {}ª PESSSOA ---------'.format(p))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('[M]/[F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
       maioridadehomem = idade
       nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff':
        if idade < 20:
            totmulher20 += 1
print('A média das idades é: {}'.format(somaidade / 4))
print('{} é o homem mais velho e tem {} anos'.format(nomevelho, maioridadehomem))
print('Há {} mulheres com menos de 20 anos'.format(totmulher20))


