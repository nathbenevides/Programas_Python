# 17-Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
#ou from math import hypot

'''co = float(input('O cateto oposto vale: '))
ca = float(input('O cateto adjacente vale: '))
h = (co**2+ca**2)**(1/2)
print('Sendo o cateto oposto {:.2f} e o cateto adjacente {:.2f}, a hiponenusa vale: {:.2f} '.format(co, ca, h))'''

co = float(input('O cateto oposto vale: '))
ca = float(input('O cateto adjacente vale: '))
h = math.hypot(co, ca)
#ou h = hypot(co, ca)
print('Sendo o cateto oposto {:.2f} e o cateto adjacente {:.2f}, a hiponenusa vale: {:.2f} '.format(co, ca, h))