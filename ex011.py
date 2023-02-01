# 11- Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

t = float(input('tamanho da parede: '))
c = float(input('comprimento da parede: '))
a = t * c
l = a/2
# 1L = 2m

print('Sendo a dimensão da sua parede {:.3f} m x {:.3f} m, a área dela é: {:.3f} m² \nsendo a área {:.3f} m², será necessário {:.3f} litros de tinta para pintar a parede'.format(t, c, a, a, l))