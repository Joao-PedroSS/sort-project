import numpy as np
from numpy import random as rd

from algorithms.bubble_sort import bubble_sort
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
    for nome_alg, func_alg in algoritmos:
        print(f"\n=== {nome_alg} ===\n")
        
        for i, vetor in enumerate(vetores, start=1):
            print(f"Teste {i}:")
            testar_algoritmo(nome_alg, func_alg, vetor)

# Lista de algoritmos
algoritmos = [
    ("Bubble Sort", bubble_sort),
    ("Insertion Sort", insertion_sort),
    ("Selection Sort", selection_sort),
    ("Quick Sort", quick_sort),
    ("Shell Sort", shell_sort),
    ("Merge Sort", merge_sort)
]

# Lista de vetores
vetores = [
    vetor1,
    vetor2,
    vetor3,
    vetor4,
    vetor5,
    vetor6,
    vetor7,
    vetor8
]

# Execução
testar_todos_algoritmos(algoritmos, vetores)