# 50- Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

cont = 0
soma = 0
for c in range (1, 7):
    n = int(input('Digite um número {}: '.format((c))))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você disse {} números pares e a soma foi {}'.format(cont, soma))
#else:

