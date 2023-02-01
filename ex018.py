# 18- Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = float(input('Quanto mede o ângulo? '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('Seu seno é: {:.2f} \nSeu cosseno é: {:.2f} \nSua tangente é: {:.2f}'.format(s, c, t))