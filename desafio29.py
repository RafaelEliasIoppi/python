vel = float(input('Digite a velocidade do carro: '))
if vel >= 80:
    print('MULTADO!!! Você excedeu o limite de velocidade de 80 KM/H')
    multa = (vel * 7) - (80 * 7) #multa é de 7,00 reais por km excedido
    print('Você deve pagar uma multa de: {:.2f} reais'.format(multa))
else:
    print('Bom dia !!!! Dirija com cuidado:')