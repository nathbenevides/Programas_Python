# 8- Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite um numero : '))
print('Analisando {} metros, seu valor em? \n km: {} \n hm: {} \n dam: {} \n dm: {} \n cm {} \n mm: {}'.format((m),(m*0.001), (m*0.01), (m*0.1), (m*10), (m*100), (m*1000)))