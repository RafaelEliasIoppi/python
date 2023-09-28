aluno = {}
aluno['nome'] = str(input('Digite o nome: '))
aluno['média'] = float(input('Digite a média do'f' {aluno["nome"]}:'))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situção'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='* 10)
for k, v in aluno.items():
    print(f' \n - {k} é igual a {v}', end=' ')




