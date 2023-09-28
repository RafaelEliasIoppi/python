import math
m = int(input('Digite o número total de elementos: '))
n = int(input('Digite o tamanho das combinaçoes: '))
c = math.factorial(m)/(math.factorial(n)*(math.factorial(m-n)))
print('A probabilidade de combinaçoes possiveis com {} números é de: {:.0f}\n A chance de acerto é: {:.8f} % '.format(n, c, ((1/c)*100)) )

