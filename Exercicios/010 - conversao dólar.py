# Crie um programa que leia quanto dinheiro uma pessoa tem em reais e mostre quantos dólares ela pode comprar. Considere U$1,00 = R$3,27.

reais = float(input('Digite quanto você possui em reais: '))
conversao = reais / 3.27

print(f' Com o valor de R${reais:.2f}, você pode comprar U${conversao:.2f}')