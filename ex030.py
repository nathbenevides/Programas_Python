# 30- Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Fale um número: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é par !'.format(numero))
else:
    print('O número {} é impar!'.format(numero))
