soma = cont = 0
while True:
    n = int(input('Digite um número qualquer ou [999] para parar: '))
    if n == 999:
        break
    else:
        soma += n
        cont += 1
print(f'Você digitou {cont} números e a soma é de : {soma}')
