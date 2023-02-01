# 40-  Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2

if media<5.0:
    print('Quem tirou as notas {} e {}, tem a média {} e está  \33[1;31mREPROVADO!\33[m'.format(nota1, nota2, media))
elif 7>media>=5.0:
    print('Quem tirou as notas {} e {}, tem a média {} e está de \33[1;33mRECUPERAÇÃO!\33[m'.format(nota1, nota2, media))
elif media>=7:
    print('Quem tirou as notas {} e {}, tem a média {} e está \33[1;32mAPROVADO!\33[m'.format(nota1, nota2, media))
