# 41-A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc
if idade <= 9:
    print('O atleta tem {} anos \n\33[7;30;32mClassificação\33[m: \33[1;33mMIRIN\33[m'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos \nClassificação\33[m: \33[1;35mINFANTIL\33[m'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos \n\33[7;30;32mClassificação\33[m: \33[1;32mJÚNIOR\33[m'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos \n\33[7;30;32mClassificação\33[m: \33[1;31mSÊNIOR\33[m'.format(idade))
else:
    print('O atleta tem {} anos \n\33[7;30;32mClassificação\33[m: \33[1;36mMASTER\33[m'.format(idade))

