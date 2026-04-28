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
            algoritmo(arr, 0, len(arr) - 1)
    return executar

def carregar_csv(caminho):
    vetores = {}

    with open(caminho, newline='') as f:
        reader = csv.DictReader(f)

        # Inicializa listas para cada coluna
        for col in reader.fieldnames:
            vetores[col] = []

        # Lê os dados
        for linha in reader:
            for col in reader.fieldnames:
                if linha[col] != "":
                    vetores[col].append(int(linha[col]))

    return vetores

#Vetores de teste
dados_csv = carregar_csv("banco_vetores_random.csv")

# Função para testar tudo
def testar_todos_algoritmos(algoritmos, vetores):
    resultado = []

    inicio = 0
    fim = 0
    for nome_alg, func_alg in algoritmos:
        print(f"\n=== {nome_alg} ===\n")
        tempoVetor = []

        for nome_vetor, vetor in vetores:
            print(f"Teste {nome_vetor}:")
            arr = vetor[:]   # cópia segura de lista

            inicio = time.time()
            func_alg(arr)
            fim = time.time()

            tempo = round((fim - inicio) * 1000, 2)

            # Mostra só os primeiros valores pra não travar
            print("Entrada:", vetor[:10], "...")
            print("Saída:", arr[:10], "...")
            print("-" * 40)

            tempoVetor.append((nome_vetor, tempo))

        resultado.append((nome_alg, tempoVetor))

    return resultado

def imprimir_tabela_cruzada(dados):
    # nomes dos testes
    testes = [nome for nome, _ in dados[0][1]]

    # largura das colunas
    largura = 12

    # cabeçalho
    print("\n")
    print(f"{'Algoritmo':<20}", end="")
    for t in testes:
        print(f"{t:<{largura}}", end="")
    print()

    print("-" * (20 + largura * len(testes)))

    # linhas
    for nome_alg, resultados in dados:
        print(f"{nome_alg:<20}", end="")

        for _, tempo in resultados:
            print(f"{tempo:<{largura}.2f}", end="")

        print()

# Lista de algoritmos
algoritmos = [
    ("Radix Sort", wrapper_geral(radix_sort)),
    ("Insertion Sort", wrapper_geral(insertion_sort)),
    ("Selection Sort", wrapper_geral(selection_sort)),
    ("Quick Sort", wrapper_geral(quick_sort)),
    ("Shell Sort", wrapper_geral(shell_sort)),
    ("Merge Sort", wrapper_geral(merge_sort))
]

# Lista de vetores
vetores = []
for nome, lista in dados_csv.items():
    vetores.append((nome, lista))

# Execução
result = testar_todos_algoritmos(algoritmos, vetores)

imprimir_tabela_cruzada(result)