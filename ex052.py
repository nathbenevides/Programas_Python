# 52-Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
tot = 0
num = int(input('Digite um número: '))
for c in range (1, num + 1):
    if num % c == 0:
        print('\33[1;32m', end=' ')
        tot += 1
    else:
        print('\33[1;31m', end=' ')
    print('{}'.format(c), end='')
print('\n\33[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('Então ele é PRIMO!')
else:
    print('Então ele NÃO É PRIMO!')


