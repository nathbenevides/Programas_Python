# 43-Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Qual seu peso? KG '))
altura = float(input('Qual sua altura? '))
imc = peso/(altura**2)
print('Seu IMC é {:.1f} você está '.format(imc))
if imc < 18.5:
    print('\33[1;33mABAIXO DO PESO\33[m')
elif 18.5 <= imc < 25:
    print('\33[1;32mNo PESO IDEAL\33[m')
elif 25 <= imc < 30:
    print('Com \33[1;32mSOBREPESO\33[m')
elif 30 <= imc <= 40:
    print('Com \33[1;31mOBESIDADE\33[m')
elif 40 <= imc:
    print('Com \33[1;31;40mOBESIDADE MÓRBIDA\33[m')
