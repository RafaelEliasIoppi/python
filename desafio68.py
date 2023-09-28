import random
cont = 0
computador = 0
while True:
      print('--=--' *6)
      computador = random.randint(0, 10)
      jogador = int(input('Vamos jogar Par ou Impar. Digite um valor: '))
      escolhe = str(input('Escolhar Par[P]/Ímpar[I]: ')).strip().upper()[0]
      soma = computador + jogador
      print(f'{jogador} + {computador} = {soma}')
      print('--=--' *6)
      if escolhe == 'P' and soma % 2 == 0:
            cont += 1
            print('--- PAR ---  VOCÊ VENCEU. PARABÉNS!!!')
      if escolhe == 'P' and soma % 2 != 0:
            print('VOCÊ PERDEU')
            break
      if escolhe == 'I' and soma % 2 == 0:
            print('VOCÊ PERDEU')
            break
      if escolhe == 'I' and soma % 2 != 0:
            cont += 1
            print(f'--- ÍMPAR --- VOCÊ GANHOU. PARABÉNS!!!')
print(f'FIM. VOCÊ GANHOU {cont} vezes')
