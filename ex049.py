#  49- Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# 9-Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número para ver sua tabuada: '))
for c in range (0, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))