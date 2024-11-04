def busca_binaria_iterativa(array, target):
    esquerda = 0
    direita = len(array) - 1
    total_comparacoes = 0

    while esquerda <= direita:
        total_comparacoes += 1
        posicao_media = (esquerda + direita) // 2

        if array[posicao_media] == target:
            return posicao_media, total_comparacoes
        elif array[posicao_media] < target:
            esquerda = posicao_media + 1
        else:
            direita = posicao_media - 1

    return -1, total_comparacoes
