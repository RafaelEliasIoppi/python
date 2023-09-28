import math
angulo = int(input('Digite o angulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(' O ângulo de {}ª graus é:\n Seno: {:.2f}\n Cos:  {:.2f}\n Tang: {:.2f}\n'.format(angulo, sen, cos, tan))

