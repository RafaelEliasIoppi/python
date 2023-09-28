from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Digite o nome:'))
nasc = int(input('Digite o ano de nascimento: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['ctps'] = int(input('Número da CTPS ( 0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['ano'] = int(input('Digite o ano de contratação: '))
    cadastro['salario'] = float(input('Digite o salário: '))
    cadastro['aposentadoria'] = ((cadastro['ano'] + 35) - datetime.now().year) + cadastro['idade']
for k, v in cadastro.items():
    print(f'{k} é igual a {v}')
print('FIM')