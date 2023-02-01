# 53- Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper() #ELIMINEI OS ESPAÇOS ANTES E DEPOIS E JOGUEI TUDO PRA MAIÚSCULO
palavras = frase.split()  #SPLITEI PRA GERAR UMA LISTA
junto = ''.join(palavras)  #JUNTEI A LISTA PRA ELIMINAR OS ESPAÇOS ANTES
#inverso = ''
inverso = junto[::-1]  #inicio, fim, inverso

'''for letra in range(len(junto) -1, -1, -1):  #FIZ O INVERSO DA FRASE
    inverso += junto[letra]'''

print('O inverso de {} é {}'. format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É PALÍNDROMO')