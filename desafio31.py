dist = int(input('Digite a distância da viagem em KM:'))
cores = {'azul':'\033[34m', 'limpa':'\033[m'}
if dist >= 200:
    p1 = dist * 0.4
    print('Sua viagem de {} KM custará: {}{}{} Reais'.format(dist, cores['azul'], p1, cores['limpa']))
else:
    p2 = dist * 0.8
    print('Sua viagem de {} KM curtará: {}{}{} Reais'.format(dist, cores['azul'], p2, cores['limpa'] ))
