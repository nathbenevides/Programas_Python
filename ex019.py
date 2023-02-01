# 19- Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
a1 = input('primeiro aluno: ')
a2 = input('segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
alunos = [a1, a2, a3, a4]
sorteio = choice(alunos)
print('O aluno sorteado foi: {}'.format(sorteio))