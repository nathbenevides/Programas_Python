# 10-Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$ 5.22 e €= 5.55
r = float(input('Quantos reais você tem ? R$ '))
print('Com R$ {:.2f} você pode comprar US$ {:.2f} e € {:.2f} '.format(r, r/5.22, r/5.55))