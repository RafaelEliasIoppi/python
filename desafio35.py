r1 = float(input('Digite a primeira reta:'))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a tereira reta:'))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r2 + r3):
    print('As três retas:  -- {} -- {} -- {} --   Podem formar um triângulo '.format(r1, r2, r3))
else:
    print('As três retas   -- {} -- {} -- {} --   Não podem formar um triângulo'.format(r1, r2, r3))