print('=' * 30)
print('{:^30}'.format('BANCO -  RAFAEL ELIAS IOPPI'))
print('=' * 30)
valor = int(input('Qual valor vc quer sacar: '))
total = valor
ced = 50
totced = 0
while True:
     if total >= ced: #verificar quantas cedulas de 50 posso tirar do valor total
        total -= ced
        totced += 1
     else:
         if total > 0:
             print('Total de {} cédulas de R$ {}'.format(totced, ced))
         if ced == 50:
              ced = 20
         elif ced == 20:
              ced = 10
         elif ced == 10:
              ced = 1
         totced = 0
         if total == 0:
              break




