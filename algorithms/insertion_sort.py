# Ideia: insere no lugar certo
# Big-O: melhor O(n), médio O(n²), pior O(n²)

def insertion_sort(arr, left, right):
    swaps = 0        # trocas lógicas (shifts / writes)
    comparisons = 0  # comparações entre elementos

    # Começa do segundo elemento
    for i in range(left + 1, right + 1):
        # Guarda o valor atual
        chave = arr[i]

        # Começa comparando com o anterior
        j = i - 1

        # Move os elementos maiores para a direita
        while j >= left:
            comparisons += 1

            if arr[j] > chave:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break

        # Insere o valor na posição correta
        arr[j + 1] = chave
        swaps += 1

    return swaps, comparisons