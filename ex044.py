# 44- Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros

preço = float(input('Preço: R$ '))
print('\33[1;35;40mFORMAS DE PAGAMENTO:\33[m')
print('''[1] à vista dinheiro/cheque
[2] à vista cartão de crédito
[3] 2x no cartão de crédito
[4] 3x ou mais do cartão de crédito''')
opçao = int(input('Qual é a opção? '))

if opçao == 1:
    print('Sua compra ', end='')
    print('à vista é R$ {:.2f}'.format(preço - (preço * 10 / 100)))
elif opçao == 2:
    print('à vista, no cartão, é R$ {:.2f}'.format(preço - (preço * 5 / 100)))
elif opçao == 3:
    print('em até 2x no cartão é R$ {:.2f}'.format(preço))
elif opçao == 4:
    parc = int(input('quantidade de parcelas: '))
    montante = preço + (preço * 20/100)
    valormes = montante / parc
    if 3<=parc:
        print('Sua compra será parcelada em {}x no cartão: \nirá custar R$ {:.2f}; o juros cobrado será de R$ {:.2f} e você irá pagar R$ {:.2f} por mês'.format(parc, montante , montante - preço, valormes))

