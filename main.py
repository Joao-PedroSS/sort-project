import numpy as np
import time 
from numpy import random as rd

from algorithms.radix_sort import radix_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort
from algorithms.quick_sort import quick_sort
from algorithms.merge_sort import merge_sort
from algorithms.shell_sort import shell_sort

#Vetores de teste
vetor1 = np.array([8, 5, 1, 7, 9, 4, 10, 3, 6, 2])
vetor2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
vetor3 = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
vetor4 = np.array([8, 5, 1, 7, 9, 4, 10, 3, 6, 2, 8, 5, 1])
vetor5 = np.array([])
vetor6 = np.array([5])
vetor7 = np.array([6, 9, 6, 7, 6, 5, 6, 6, 2, 6])
vetor8 = rd.randint(0, 1000, 100)

#Função para testar individual 
def testar_algoritmo(nome, algoritmo, vetor):
    arr = vetor.copy()
    
    print(f"{nome}")
    print("Entrada: ", vetor)
    
    if len(arr) > 0:
        algoritmo(arr, 0, len(arr) - 1)
    
    print("Saída:  ", arr)
    print("-" * 40)


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
            inicio = time.time()

            testar_algoritmo(nome_alg, func_alg, vetor)
            
            fim = time.time()
            tempo = round((fim - inicio) * 1000, 2)

            tempoVetor.append((nome_vetor, tempo))

        resultado.append((nome_alg, tempoVetor))

    return resultado

def imprimir_tabela_cruzada(dados):
    # Pega todos os nomes de testes (usando o primeiro algoritmo como base)
    testes = [nome if nome else "Caso X" for nome, _ in dados[0][1]]

    # Cabeçalho
    print("\n\n")
    header = ["Algoritmo"] + testes
    print(" | ".join(f"{h:<18}" for h in header))
    print("-" * (20 * len(header)))

    # Linhas
    for nome_alg, resultados in dados:
        linha = [nome_alg]

        for nome_teste, tempo in resultados:
            linha.append(f"{tempo:.2f}")

        print(" | ".join(f"{col:<18}" for col in linha))

# Lista de algoritmos
algoritmos = [
    ("Bubble Sort", radix_sort),
    ("Insertion Sort", insertion_sort),
    ("Selection Sort", selection_sort),
    ("Quick Sort", quick_sort),
    ("Shell Sort", shell_sort),
    ("Merge Sort", merge_sort)
]

# Lista de vetores
vetores = [
    ("Aleatório curto", vetor1),
    ("Ordenado", vetor2),
    ("Decrescente", vetor3),
    ("", vetor4),
    ("Vazio", vetor5),
    ("Um valor", vetor6),
    ("Repetidos", vetor7),
    ("Aleatório longo", vetor8)
]

# Execução
result = testar_todos_algoritmos(algoritmos, vetores)

imprimir_tabela_cruzada(result)