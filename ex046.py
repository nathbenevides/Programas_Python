# 46-Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\33[1;30;42mBUM!\33[m \33[1;30;41mBUM!\33[m \33[1;30;45mPOOOW!\33[m')
sleep(1)
