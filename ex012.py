# 12- Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('preço do produto: R$ '))
d = p-(p*5/100)
print('Esse produto no preço de R${:.2f} com 5% de desconto sai a R${:.2f}'.format(p, d))