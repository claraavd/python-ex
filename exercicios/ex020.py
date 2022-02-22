import random
a=str(input('Digite o nome do pmeiro aluno(a): '))
b=str(input('Digite o nome do segundo aluno(a): '))
c=str(input('Digite o nome do terceiro aluno(a): '))
d=str(input('Digite o nome do quarto aluno(a): '))
mylist=[a,b,c,d]
random.shuffle(mylist)
print('A ordem de apresentação será:')
print(mylist)