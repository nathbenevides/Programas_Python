# 35- Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-'* 60)
print('\33[1;35;40mAnalisador de triângulos\33[m')
print('-'*60)
n1 = int(input('comprimento 1: '))
n2 = int(input('Comprimento 2: '))
n3 = int(input('Comprimento 3: '))
if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print('Os comprimentos acima \33[1;30;42m PODEM FORMAR \33[m um triagulo')
else:
    print('Os comprimentos acima \33[1;30;41m NÃO PODEM \33[m formar um triângulo')

