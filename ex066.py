#66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

n = s = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Você digitou {c} números e a soma entre eles vale {s}')
