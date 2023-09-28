from time import sleep
n = int(input('Digite o número inicial:'))
for c in range(n, -1, -1):
    print(c)
    sleep(0.5)
print('ACABOU')
