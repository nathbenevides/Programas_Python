# 42-  Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO
#ISÓSCELES
#ESCALENO
# 35-Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-'*24)
print('\33[1;35;40mANALISADOR DE TRIÂNGULOS\33[m')
print('-'*24)
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas formam um triângulo: ', end='')
    if r1 == r2 == r3:
        print('\33[1;35mEQUILÁTERO\33[m')
    elif r1 != r2 != r3 != r1:
        print('\33[1;35mESCALENO\33[m')
    else:
        print('\33[1;35mISÓSCELES\33[m')
else:
    print('As retas NÃO formam um triângulo')

