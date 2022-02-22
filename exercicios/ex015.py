n=int(input('Quantos dias o carro ficou alugado?'))
m=float(input('Quantos km o carro rodou?'))
p=60*n+0.15*m
print('Ao rodar {} km durante {:.2f} dias, você deve pagar R${:.2f}.'.format(m,n,p))