# 29- Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade do carro? km '))
multa = 7 * (velocidade - 80)
if velocidade > 80:
    print('Você foi multado em R$ {:.2f}'.format(multa))
print('Tenha um bom dia e dirija com segurança!')