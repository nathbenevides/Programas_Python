#64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = 0
soma = 0
cont = 0
n = int(input('Digite um número [999] para parar: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número [999] para parar: '))
print(f'Você digitou {cont} números e a soma deles foi {soma}')