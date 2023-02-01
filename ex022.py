#Crie um programa que leia o nome completo de uma pessoa e mostre:

#O nome com todas as letras maiúsculas e minúsculas.

#Quantas letras ao todo (sem considerar espaços).

#Quantas letras tem o primeiro nome.

nome = str(input('Qual seu nome completo? ')).strip()
print('MAIÚSCULO: {}'.format(nome.upper()))
print('minúsculo: {}'.format(nome.lower()))
print('Possui {} letras ao todo'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))