"""
CheckPoint 1 - Dynamic Programming
Aluno: Lucca - RM: 560731

Estrutura:
- Parte 1.1: Ordenação de pontos pela distância de Manhattan
- Parte 1.2: Ordenação de palavras por ordem personalizada
- Parte 2.1: Comparação de Merge vs Quick (pontos)
- Parte 2.2: Comparação de Merge vs Quick (palavras)
"""

import time
import sys

# ============================================================
# PARTE 1.1 - Ordenação de Pontos pela Distância de Manhattan
# ============================================================

# Input (RM ímpar → 13 pontos)
points_tuple = (
    (-2.5, 3.1),
    (0.0, -4.2),
    (5.5, -1.2),
    (-3.3, -3.3),
    (2.0, 2.0),
    (0.5, 0.5),
    (-7.1, 0.2),
    (4.4, 4.4),
    (-1.0, 0.0),
    (3.1415, -2.718),
    (-0.001, 0.001),
    (6.0, -6.0),
    (1.1, -8.8),
)

# 1) Distância de Manhattan: |x| + |y|
distances = {}
for pt in points_tuple:
    distances[pt] = abs(pt[0]) + abs(pt[1])

# 2) Exemplo de list comprehension para reestruturar
points_with_dist = [(pt, distances[pt]) for pt in points_tuple]

# Funções Merge Sort e Quick Sort (recursivas)
def merge_sort_points(lst):
    if len(lst) <= 1:
        return lst[:]
    mid = len(lst) // 2
    left = merge_sort_points(lst[:mid])
    right = merge_sort_points(lst[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if distances[left[i]] <= distances[right[j]]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def quick_sort_points(lst):
    if len(lst) <= 1:
        return lst[:]
    pivot = lst[len(lst)//2]
    menores = [x for x in lst if distances[x] < distances[pivot]]
    iguais = [x for x in lst if distances[x] == distances[pivot]]
    maiores = [x for x in lst if distances[x] > distances[pivot]]
    return quick_sort_points(menores) + iguais + quick_sort_points(maiores)

print("\n=== PARTE 1.1 ===")
print("Pontos originais:", points_tuple)
print("Dicionário ponto -> distância:", distances)
print("Exemplo de list comprehension (ponto, distância):", points_with_dist)
print("\nMerge Sort result:", merge_sort_points(list(points_tuple)))
print("Quick Sort result:", quick_sort_points(list(points_tuple)))


# ============================================================
# PARTE 1.2 - Ordenação de Palavras por Ordem Personalizada
# ============================================================

# Input (RM ímpar → lista de palavras + dicionário)
words_input = [
    "melao", "bistro", "cereja", "abacaxi", "misto",
    "bolo de sorvete", "mingau", "cerveja", "melaço",
    "pera", "biscoito", "palito de chocolate"
]
prioridade = {'a': 1, 'b': 2, 'c': 3, 'e': 4,
              'h': 5, 'l': 6, 'm': 7, 'p': 8,
              'r': 9, 'y': 10}

# Hipótese: ignoramos acentos e comparamos apenas letras minúsculas
def normalizar(palavra):
    nova = ""
    for ch in palavra.lower():
        if ch in "áàãâ": nova += "a"
        elif ch in "éê": nova += "e"
        elif ch in "í": nova += "i"
        elif ch in "óõô": nova += "o"
        elif ch in "ú": nova += "u"
        elif ch == "ç": nova += "c"
        else: nova += ch
    return nova

def prioridade_palavra(palavra):
    return [prioridade.get(ch, 999) for ch in normalizar(palavra)]

priority_vectors = {w: prioridade_palavra(w) for w in words_input}

def comparar(w1, w2):
    v1, v2 = priority_vectors[w1], priority_vectors[w2]
    for a, b in zip(v1, v2):
        if a < b: return -1
        if a > b: return 1
    return len(v1) - len(v2)

def merge_sort_words(lst):
    if len(lst) <= 1:
        return lst[:]
    mid = len(lst) // 2
    left = merge_sort_words(lst[:mid])
    right = merge_sort_words(lst[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if comparar(left[i], right[j]) <= 0:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:]); merged.extend(right[j:])
    return merged

def quick_sort_words(lst):
    if len(lst) <= 1:
        return lst[:]
    pivot = lst[len(lst)//2]
    menores = [x for x in lst if comparar(x, pivot) < 0]
    iguais = [x for x in lst if comparar(x, pivot) == 0]
    maiores = [x for x in lst if comparar(x, pivot) > 0]
    return quick_sort_words(menores) + iguais + quick_sort_words(maiores)

print("\n=== PARTE 1.2 ===")
print("Palavras originais:", words_input)
print("Vetores de prioridade:", priority_vectors)
print("\nMerge Sort result:", merge_sort_words(words_input))
print("Quick Sort result:", quick_sort_words(words_input))


# ============================================================
# PARTE 2.1 e 2.2 - Comparação de Desempenho
# ============================================================

print("\n=== PARTE 2.1 (Pontos) ===")
print("- Merge Sort sempre O(n log n), usa listas auxiliares (mais memória).")
print("- Quick Sort na média também O(n log n), mas pior caso O(n^2).")
print("- Em listas pequenas como esta (13 pontos), o tempo é praticamente o mesmo.")

print("\n=== PARTE 2.2 (Palavras) ===")
print("- Mesma análise: Merge é mais previsível e estável, Quick pode variar mais.")
print("- Como o input é pequeno, diferença prática de tempo/memória é mínima.")
print("- Mas em inputs grandes, Quick costuma ser mais rápido em média.")

# ============================================================
# CONCLUSÃO
# ============================================================

print("\n=== CONCLUSÃO FINAL ===")
print("- Merge Sort é estável e seguro no pior caso.")
print("- Quick Sort é eficiente na média, mas pode ser pior em alguns cenários.")
print("- Usamos list comprehension para reestruturar dados (pontos e palavras).")
print("- Guardamos os pontos em tupla (imutável) e usamos dicionário para mapear distâncias.")
print("- Hipótese: normalização de acentos para aplicar corretamente o dicionário de prioridade.")
