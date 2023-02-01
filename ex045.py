# 45- Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua jogada ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-'*20)
print('O PC jogou \33[1;30;45m{}\33[m'.format(itens[pc]))
print('Você jogou \33[1;30;44m{}\33[m'.format(itens[jogador]))
print('-'*20)
if pc == 0:  #PC jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Você VENCEU')
    elif jogador == 2:
        print('Computador VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

elif pc == 1:  #PC jogou PAPEL
    if jogador == 0:
        print('Computador VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Você VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

elif pc == 2:  #PC jogou TESOURA
    if jogador == 0:
        print('Você VENCEU')
    elif jogador == 1:
        print('Computador VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')

