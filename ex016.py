# 16-Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#import math

from math import trunc
nr = float(input('digite um numero: '))
print('a porção inteira de {} é {}'.format(nr, trunc(nr)))

#ou
'''print('a porção inteira de {} é {}'.format(nr, int(nr)))'''

