from math import hypot
o= float(input('Qual o comprimento do cateto oposto?'))
a=float(input('Qual o comprimento do cateto adjacente?'))
h=hypot(o,a)
print('A hipotenusa de um triângulo com catetos iguais a {:.1f} e {:.1f} é {:.1f}.'.format(o,a,h))