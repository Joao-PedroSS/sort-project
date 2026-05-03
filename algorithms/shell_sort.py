# Ideia: usa saltos (gap)
# Big-O: aproximaamente O(n log n) a O(n²)

def shell_sort(arr, left, right):
    swaps = 0        # trocas lógicas (shifts / writes)
    comparisons = 0  # comparações entre elementos

    # Tamanho do trecho
    n = right - left + 1

    # Define o gap inicial
    gap = n // 2

    # Enquanto o gap for maior que 0
    while gap > 0:

        # Percorre o vetor com base no gap
        for i in range(left + gap, right + 1):
            # Guarda o valor atual
            temp = arr[i]

            j = i

            # Move elementos maiores usando o gap
            while j >= left + gap:
                comparisons += 1

                if arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    swaps += 1
                    j -= gap
                else:
                    break

            # Insere na posição correta
            arr[j] = temp
            swaps += 1

        # Diminui o gap
        gap //= 2

    return swaps, comparisons