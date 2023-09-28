#PROBABILIDADE BINOMIAL
import math
n = int(input('Digite o número de tentativas: ')) # Tentivas independentes
p = float(input('Digite a probabilidade de sucesso: '))
q = float(input('Digite a probabilidade de fracasso: '))
x = int(input('Digite a quantidade de sucesso: '))
probabilidade = ((math.factorial(n)/(math.factorial(n-x)*math.factorial(x)))*math.pow(p,x)*math.pow(q,(n-x)))
print('A probabilidade de sucesso é: {:.4f}\n em porcentagem:  {:.2f}%'.format(probabilidade, probabilidade*100))



