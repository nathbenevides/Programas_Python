# 13- Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Qual seu sálario? R$'))
a = s+(s*15/100)
print('Com o aumento de 15%, seu salário passa a ser de R${:.2f} para R${:.2f}'.format(s, a))