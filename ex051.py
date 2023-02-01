# 51- Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('-='*11)
print('\33[1;30;45m 10 TERMOS DE UMA PA \33[m')
print('-='*11)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end= ' ♥ ')
print('\33[1;30mFIM\33[m')