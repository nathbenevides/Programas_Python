# 34- Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00,calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salário = float(input('Qual o seu salário? R$ '))
if salário >= 3234:
    aumento = (3234 * 8/100)
    novo = salário + aumento
if salário < 3234:
    aumento = (3234 * 15/100)
    novo = salário + aumento
print('Com base no salário de R$ {:.2f}, você recebeu um aumento de {:.2f} e passou a ganhar {:.2f}'.format(salário, aumento, novo))
