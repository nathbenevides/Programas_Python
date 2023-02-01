# 54- Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

'''totmaior = 0
totmenor = 0
for c in range (1, 8):
    nasc = int(input('Digite sua data de nascimento: '))
    if nasc <= 2005:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas MAIORES de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas MENORES de idade'.format(totmenor))'''

#ou

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for p in range(1, 8):
    nasc = int(input('Digite sua data de nascimento: '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas MAIORES de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas MENORES de idade'.format(totmenor))
