import math
x=float(input('Digite um ângulo: '))
xpi=math.radians(x)
spi=math.sin(xpi)
cpi=math.cos(xpi)
tpi=math.tan(xpi)
print('O seno de {:.2f} é {:.2f}.'.format(x,math.degrees(spi)))
print('O cosseno de {:.2f} é {:.2f}.'.format(x,math.degrees(cpi)))
print('A tangente de {:.2f} é {:.2f}.'.format(x,math.degrees(tpi)))