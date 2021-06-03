# Crie um programa que receba o valor de um produto e mostre seu valor final com 5% de desconto.

preco = float(input('Qual o preço do produto? '))
preco_final = preco * 0.95
print(f'O valor final do seu produto com 5% de desconto é R${preco_final:.2f}')