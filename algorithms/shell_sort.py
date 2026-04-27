# Ideia: usa saltos (gap)
# Big-O: aproximaamente O(n log n) a O(n²)

def shell_sort(arr, left, right):
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
            while j >= left + gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # Insere na posição correta
            arr[j] = temp

        # Diminui o gap
        gap //= 2