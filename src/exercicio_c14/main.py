import numpy as np

qtd = int(input('Quantidade de números do vetor: '))
numeros = []

for i in range(qtd):
    numero = int(input(f'Digite o número: '))
    numeros.append(numero)

array = np.array(numeros)

print (array)