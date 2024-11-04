def busca_binaria_recursiva(arr, alvo, esquerda=0, direita=None, contagem=0):
    if direita is None:
        direita = len(arr) - 1
    if esquerda > direita:
        return -1, contagem

    meio_indice = (esquerda + direita) // 2
    contagem += 1

    if arr[meio_indice] == alvo:
        return meio_indice, contagem
    elif arr[meio_indice] < alvo:
        return busca_binaria_recursiva(arr, alvo, meio_indice + 1, direita, contagem)
    else:
        return busca_binaria_recursiva(arr, alvo, esquerda, meio_indice - 1, contagem)
