def area(a, b):
    c = a * b
    print(f'A área do terreno de {a:.2}m X {b:.2}m é de: {c:.3}m²')

print('CÁCULO DE ÁREA DE UM TERRENO')
print('--' * 10)
a1 = float(input('Largura (m): '))
a2 = float(input('Comprimento (m): '))
print('--' * 10)
area(a1, a2)
