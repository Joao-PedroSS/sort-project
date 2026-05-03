import time
import csv
import os

print(os.getcwd())

from algorithms.radix_sort import radix_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort
from algorithms.quick_sort import quick_sort
from algorithms.merge_sort import merge_sort
from algorithms.shell_sort import shell_sort


def wrapper_geral(algoritmo):
    def executar(arr):
        if len(arr) > 0:
            return algoritmo(arr, 0, len(arr) - 1)
        return 0, 0

    return executar


def carregar_csv(caminho):
    vetores = {}

    with open(caminho, newline="") as f:
        reader = csv.DictReader(f)

        for col in reader.fieldnames:
            vetores[col] = []

        for linha in reader:
            for col in reader.fieldnames:
                if linha[col] != "":
                    vetores[col].append(int(float(linha[col])))


    return vetores


dados_csv = carregar_csv("banco_dados_ordenacao.csv")


def testar_todos_algoritmos(algoritmos, vetores):
    resultado = []

    for nome_alg, func_alg in algoritmos:
        print(f"\n=== {nome_alg} ===\n")
        resultados_por_vetor = []

        for nome_vetor, vetor in vetores:
            print(f"Teste {nome_vetor}:")
            arr = vetor[:]

            inicio = time.time()
            swaps, comparisons = func_alg(arr)
            fim = time.time()

            tempo = round((fim - inicio) * 1000, 2)

            print("Entrada:", vetor[:10], "...")
            print("Saida:", arr[:10], "...")
            print(f"Swaps: {swaps}")
            print(f"Comparisons: {comparisons}")
            print("-" * 40)

            resultados_por_vetor.append(
                {
                    "teste": nome_vetor,
                    "tempo": tempo,
                    "swaps": swaps,
                    "comparisons": comparisons,
                }
            )

        resultado.append((nome_alg, resultados_por_vetor))

    return resultado


def imprimir_tabela_cruzada(dados):
    largura_algoritmo = 18
    largura_teste = 14
    largura_tempo = 12
    largura_swaps = 12
    largura_comparisons = 14

    print("\nResumo dos testes")
    print(
        f"{'Algoritmo':<{largura_algoritmo}}"
        f"{'Teste':<{largura_teste}}"
        f"{'Tempo(ms)':<{largura_tempo}}"
        f"{'Swaps':<{largura_swaps}}"
        f"{'Comparisons':<{largura_comparisons}}"
    )
    print(
        "-" * (
            largura_algoritmo
            + largura_teste
            + largura_tempo
            + largura_swaps
            + largura_comparisons
        )
    )

    for nome_alg, resultados in dados:
        for resultado in resultados:
            print(
                f"{nome_alg:<{largura_algoritmo}}"
                f"{resultado['teste']:<{largura_teste}}"
                f"{resultado['tempo']:<{largura_tempo}.2f}"
                f"{resultado['swaps']:<{largura_swaps}}"
                f"{resultado['comparisons']:<{largura_comparisons}}"
            )


algoritmos = [
    ("Radix Sort", wrapper_geral(radix_sort)),
    ("Insertion Sort", wrapper_geral(insertion_sort)),
    ("Selection Sort", wrapper_geral(selection_sort)),
    ("Quick Sort", wrapper_geral(quick_sort)),
    ("Shell Sort", wrapper_geral(shell_sort)),
    ("Merge Sort", wrapper_geral(merge_sort)),
]

vetores = []
for nome, lista in dados_csv.items():
    vetores.append((nome, lista))

result = testar_todos_algoritmos(algoritmos, vetores)

imprimir_tabela_cruzada(result)
