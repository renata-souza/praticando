# n1 = input('Digite um valor: ')
# n2 = input('Digite outro valor: ')
# soma = n1 + n2
# print('A soma é:', soma)
# Nesse formato, o conteúdo das variáveis n1 e n2 são strings, pois não estão formatadas como números inteiros. Por causa disso, o resultado da variável 'soma' será uma concatenação, e não uma adição. Para resolver isso, utilizamos o tipo primitivo INT antes da criação do input.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
print(f'A soma de {n1} + {n2} é: {soma}')
