# 20- O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
# leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
a1 = input('primeiro aluno: ')
a2 = input ('segundo aluno: ')
a3 = input('terceiro aluno: ')
a4 = input('quarto aluno: ')
nomes = [a1, a2, a3, a4]
shuffle(nomes)

print('A ordem de apresentação será: {}'.format(nomes))
