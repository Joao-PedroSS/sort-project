# Ideia: insere no lugar certo
# Big-O: melhor O(n), médio O(n²), pior O(n²)

def insertion_sort(arr, left, right):
    # Começa do segundo elemento
    for i in range(left + 1, right + 1):
        # Guarda o valor atual
        chave = arr[i]

        # Começa comparando com o anterior
        j = i - 1

        # Move os elementos maiores para a direita
        while j >= left and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1

        # Insere o valor na posição correta
        arr[j + 1] = chave