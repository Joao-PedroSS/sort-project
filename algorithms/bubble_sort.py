# Ideia: troca vizinhos até ordenar
# Big-O: melhor O(n), médio O(n²), pior O(n²)

def bubble_sort(arr, left, right):
    # Se o intervalo for inválido, não faz nada
    if left >= right:
        return

    # Controla se houve troca
    swapped = True

    # Repete enquanto houver trocas
    while swapped:
        swapped = False

        # Percorre o vetor comparando vizinhos
        for i in range(left, right):
            # Se estiver fora de ordem, troca
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True  # Marca que houve troca