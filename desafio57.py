sex = ''
while sex != 'M' and sex != 'F': #repete quanto o sexo for difereten de m ou f
    sex = str(input('Digite o sexo [M]/[F]: ')).strip().upper()[0] # le o sexo e joga pra maiscula a primeira letra e tira os espaço
    if sex != 'M' and sex != 'F':
       print('Dados inválidos. Digite novamente')
    else:
       idade = int(input('Digite a idade:'))
       print('Sua idade é: {}\n O sexo é: {}'.format(idade, sex))
       print('FIM')