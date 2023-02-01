# 58- 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
pc = randint(0, 10)
print('-' * 60)
print('Vou pensar em um número entre 0 e 10. tente adivinhar...')
print('-' * 60)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Em que numero pensei? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente mais uma vez.')
        elif jogador > pc:
            print('Menos... Tente mais uma vez')
print('Parabens!! Acertou com {} palpites'. format(palpites))