# Ideia: divide pelo pivô
# Big-O: melhor/médio O(n log n), pior O(n²)

def quick_sort(arr, left, right):
    # Se o intervalo for inválido, não faz nada
    if left >= right:
        return

    # Particiona o vetor e pega a posição do pivô
    pivot_index = partition(arr, left, right)

    # Ordena a parte esquerda
    quick_sort(arr, left, pivot_index - 1)

    # Ordena a parte direita
    quick_sort(arr, pivot_index + 1, right)


def partition(arr, left, right):
    # Escolhe o pivô (último elemento)
    pivot = arr[right]

    # Índice do menor elemento
    i = left - 1

    # Percorre o vetor
    for j in range(left, right):
        # Se o elemento for menor que o pivô
        if arr[j] < pivot:
            i += 1
            # Troca para colocar na parte esquerda
            arr[i], arr[j] = arr[j], arr[i]

    # Coloca o pivô na posição correta
    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    # Retorna a posição do pivô
    return i + 1