# 7- Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
print('A média entre as notas {:.1f} e {:.1f} é {:.1f} '.format(n1, n2, (n1+n2)/2))