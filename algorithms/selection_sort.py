# Ideia: escolhe o menor
# Big-O: O(n²) em todos os casos

def selection_sort(arr, left, right):
    # Percorre todas as posições
    for i in range(left, right + 1):
        # Assume que o menor é o atual
        menor = i

        # Procura o menor no restante do vetor
        for j in range(i + 1, right + 1):
            if arr[j] < arr[menor]:
                menor = j

        # Troca o menor encontrado com a posição atual
        if menor != i:
            arr[i], arr[menor] = arr[menor], arr[i]