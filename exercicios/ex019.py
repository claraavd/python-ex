import random
a=input('Digite o nome do pmeiro aluno(a): ')
b=input('Digite o nome do segundo aluno(a): ')
c=input('Digite o nome do terceiro aluno(a): ')
d=input('Digite o nome do quarto aluno(a): ')
mylist=a,b,c,d
print('O aluno(a) sorteado foi {}.'.format(random.choice(mylist)))