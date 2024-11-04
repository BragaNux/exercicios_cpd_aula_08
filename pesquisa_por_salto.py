import math

def busca_por_salto(arr, alvo):
    tamanho = len(arr)
    salto = int(math.sqrt(tamanho))
    total_comparacoes = 0
    prev = 0

    while arr[min(salto, tamanho) - 1] < alvo:
        total_comparacoes += 1
        prev = salto
        salto += int(math.sqrt(tamanho))
        if prev >= tamanho:
            return -1, total_comparacoes

    while arr[prev] < alvo:
        total_comparacoes += 1
        prev += 1
        if prev == min(salto, tamanho):
            return -1, total_comparacoes

    total_comparacoes += 1
    if arr[prev] == alvo:
        return prev, total_comparacoes
    return -1, total_comparacoes

# Exemplo de uso
arr_exemplo = [2, 4, 6, 8, 10, 12, 14, 16]
alvo_busca = 4
indice, comparacoes = busca_por_salto(arr_exemplo, alvo_busca)

if indice != -1:
    print(f"Alvo encontrado na posição {indice} com {comparacoes} comparações.")
else:
    print("Alvo não encontrado.")
