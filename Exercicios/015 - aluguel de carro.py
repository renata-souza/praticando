# Crie um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos km você andou com o carro? '))
diaria = dias * 60
preco_km = km * 0.15
total = diaria + preco_km

print(f'Valor total de diárias = R${diaria:.2f}')
print(f'Valor total pela kilometragem percorrida = R${preco_km:.2f}')
print(f'O valor total da sua locação é de R${total:.2f}')
