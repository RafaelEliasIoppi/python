times = ('Internacional', 'Corinthians', 'Ipiranga', 'Chapecoense',
         'Grêmio', 'Náutico', 'Bahia', 'Esporte', 'Brasil de Pelotas',
         'Atlético MG', 'Coritiba', 'Havaí', 'Paraná','Figueirense',
         'Juventude', 'Caxias')
print('Os 5 primeiros colocados são: {}'.format(times[0:4]))
print('-=' *50)
print('os 4 últimos são: {}'.format(times[-4:]))
print('-=' *50)
print('Times em ordem alfabética: {}'.format(sorted(times)))
print('-=' *50)
print('A chapecoense está na {}º posição'.format(times.index('Chapecoense') + 1))


