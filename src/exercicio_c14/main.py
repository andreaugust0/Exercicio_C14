import numpy as np

def criar_array(numeros: list[int]) -> np.ndarray:
    return np.array(numeros)

def calcular_estatisticas(array: np.ndarray) -> dict:
    return {
        "soma": int(np.sum(array)),
        "media": float(np.mean(array)),
        "maximo": int(np.max(array)),
    }

if __name__ == "__main__":
    qtd = int(input('Digite uma quantidade de elementos: '))
    numeros = []

    for i in range(qtd):
        numero = int(input(f'Digite o número: '))
        numeros.append(numero)

    array = criar_array(numeros)
    print("Array:", array)

    estatisticas = calcular_estatisticas(array)
    print("Estatísticas:", estatisticas)


