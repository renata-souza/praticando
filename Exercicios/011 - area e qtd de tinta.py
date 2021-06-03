# Faça um programa que receba a altura e largura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura? '))
area = largura * altura
tinta = area / 2

print(f'A área da sua parede é de {area}m², e você precisará de {tinta} litros de tinta para pintá-la')

