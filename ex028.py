# 28-Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
pc = randint(0, 5) #faz o pc "pensar"
print('-' * 60)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-' * 60)
gamer = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3)
if gamer == pc:
    print('Parabéns!! Você conseguiu me vencer !')
else:
    print('Ganhei ! Pensei no numero {} e não no {}'.format(pc, gamer))

