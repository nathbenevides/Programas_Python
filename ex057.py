# 57-Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.


s = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Dados inválidos! Por favor, informe seu sexo [F/M]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(s))
