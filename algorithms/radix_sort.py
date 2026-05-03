# Ideia: ordena dígito por dígito (do menos significativo para o mais significativo)
# usando um método estável (counting sort)
# Big-O: melhor O(nk), médio O(nk), pior O(nk)  (k = número de dígitos)

def radix_sort(arr, left, right):
    # Se o intervalo for inválido, não faz nada
    if left >= right:
        return 0, 0  # (trocas_logicas, comparacoes)

    # Encontra o maior número no intervalo
    max_val = max(arr[left:right+1])

    # Começa pelo dígito menos significativo
    exp = 1

    total_swaps = 0
    total_comparisons = 0  # radix não usa comparações entre elementos

    # Continua enquanto ainda houver dígitos
    while max_val // exp > 0:
        swaps, comps = counting_sort(arr, left, right, exp)
        total_swaps += swaps
        total_comparisons += comps
        exp *= 10

    return total_swaps, total_comparisons


def counting_sort(arr, left, right, exp):
    n = right - left + 1

    # Vetor auxiliar
    output = [0] * n

    # Contagem dos dígitos (0–9)
    count = [0] * 10

    swaps = 0        # writes
    comparisons = 0  # não há comparação entre elementos

    # Conta ocorrências dos dígitos
    for i in range(left, right + 1):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Soma acumulada
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Monta o output (de trás pra frente = estável)
    for i in range(right, left - 1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        swaps += 1  # escrita no output

    # Copia de volta para o array original
    for i in range(n):
        arr[left + i] = output[i]
        swaps += 1  # escrita no array original

    return swaps, comparisons