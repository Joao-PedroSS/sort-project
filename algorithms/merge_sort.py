# Ideia: divide o array em partes menores, ordena e depois junta
# Big-O: melhor O(n log n), médio O(n log n), pior O(n log n)

def merge_sort(arr, left, right):
    # Se o intervalo tiver 1 ou 0 elementos, já está ordenado
    if left >= right:
        return 0, 0  # (trocas_logicas, comparacoes)

    # Divide o array no meio
    mid = (left + right) // 2

    # Ordena as duas metades
    left_swaps, left_comp = merge_sort(arr, left, mid)
    right_swaps, right_comp = merge_sort(arr, mid + 1, right)

    # Junta as partes
    merge_swaps, merge_comp = merge(arr, left, mid, right)

    # Soma tudo
    total_swaps = left_swaps + right_swaps + merge_swaps
    total_comp = left_comp + right_comp + merge_comp

    return total_swaps, total_comp


def merge(arr, left, mid, right):
    # Cria listas auxiliares (forçando lista Python, não numpy slice direto)
    left_part = [arr[i] for i in range(left, mid + 1)]
    right_part = [arr[i] for i in range(mid + 1, right + 1)]

    i = 0
    j = 0
    k = left

    swaps = 0        # trocas lógicas (writes no array principal)
    comparisons = 0  # comparações entre elementos

    # Junta ordenando
    while i < len(left_part) and j < len(right_part):
        comparisons += 1  # comparação entre elementos

        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1

        swaps += 1  # cada escrita no array conta como "troca lógica"
        k += 1

    # Copia resto da esquerda
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
        swaps += 1

    # Copia resto da direita
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1
        swaps += 1

    return swaps, comparisons