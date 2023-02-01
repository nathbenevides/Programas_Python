# 15-Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos km foram percorridos ? km '))
d = int(input('Quantos dias alugados? '))
pg = (d*60)+(km*0.15)

print('Tendo rodado {:.2f} km por {} dias, o valor à ser pago será: R$ {:.2f}'.format(km, d, pg))