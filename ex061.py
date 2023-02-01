# 61- Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
#51- Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('-='*20)
print('TERMOS DE UMA PA')
print('-='*20)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:  #enquanto o contador não chegar a 10 
    print(f'{termo} → ', end='')
    termo += razão
    cont += 1
print('FIM')