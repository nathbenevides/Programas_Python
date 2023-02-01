# 31-Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distância = float(input('Quantos Km você irá viajar? '))
print('Você irá realizar uma viagem de {} KM'.format(distancia))
if distância <= 200:
   preço = 0.50 * distância
else:
    preço = 0.45 * distância
print('A passagem irá custar: R$ {:.2f}'.format(preço))

#ou simplificado
'''preço = distância * 0.50 if distancia <= 200 else distância * 0.45'''



