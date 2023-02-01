# 25- Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Qual seu nome? ')).strip()
print('Olá {} seu nome tem Silva? {}'.format(nome, 'SILVA' in nome.upper()))

