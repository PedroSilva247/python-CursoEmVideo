import math
an = float(input('Digite um valor de um ângulo: '))
a = math.radians(an)
print('SENO {:.2f}\nCOSSENO {:.2f}\nTANGENTE {:.2f}'.format(math.sin(a), math.cos(a), math.tan(a)))
