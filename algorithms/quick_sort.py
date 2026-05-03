# Ideia: divide pelo pivô
# Big-O: melhor/médio O(n log n), pior O(n²)

def quick_sort(arr, left, right):
    # Se o intervalo for inválido, não faz nada
    if left >= right:
        return 0, 0  # (trocas_logicas, comparacoes)

    # Particiona o vetor e pega a posição do pivô
    pivot_index, swaps, comps = partition(arr, left, right)

    # Ordena a parte esquerda
    left_swaps, left_comps = quick_sort(arr, left, pivot_index - 1)

    # Ordena a parte direita
    right_swaps, right_comps = quick_sort(arr, pivot_index + 1, right)

    # Soma tudo
    total_swaps = swaps + left_swaps + right_swaps
    total_comps = comps + left_comps + right_comps

    return total_swaps, total_comps


def partition(arr, left, right):
    # Escolhe o pivô (último elemento)
    pivot = arr[right]

    # Índice do menor elemento
    i = left - 1

    swaps = 0        # trocas reais
    comparisons = 0  # comparações com o pivô

    # Percorre o vetor
    for j in range(left, right):
        # Se o elemento for menor que o pivô
        comparisons += 1
        if arr[j] < pivot:
            i += 1
            # Troca para colocar na parte esquerda
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1

    # Coloca o pivô na posição correta
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    swaps += 1

    # Retorna a posição do pivô
    return i + 1, swaps, comparisons