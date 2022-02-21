h=float(input('Quantos metros de altura tem a parede?'))
l=float(input('Quantos metros de largura tem a parde?'))
a=h*l
t=a/2
print('A parede tem um total de {:.2f} m² e precisará de {:.2f} litros de tinta em sua pintura.'.format(a,t))