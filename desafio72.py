cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito','nove', 'dez','onze', 'doze', 'treze',
           'quatorze','quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
  num = int(input('Digite um número entre 0 a 20:  '))
  if 0 <= num <= 20:
        print('{}'.format(cont[num]))
        break
  print('Tente novamente...', end=' ')
print('FIM')

