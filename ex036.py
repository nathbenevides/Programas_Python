# 36- Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa que vai comprar? '))
salário = float(input('Qual seu salário? '))
anos = int(input('em quantos anos pretende pagar? '))
prestação = casa/(anos*12)
print('Para pagar uma casa de R${:.2f} em {} anos,'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação>30/100*salário:
    print('\33[1;30;41mInfelizmente seu impréstimo não foi aprovado!\33[m')
else:
    print('\33[1;30;42mParabéns! Seu empréstimo foi aprovado!\33[m')
