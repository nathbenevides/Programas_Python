# 33- Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
c = int(input('Terceiro numero: '))
#Verificando quem é o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
        maior = c
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))
