def busca_interpolada(arr, alvo):
    esquerda = 0
    direita = len(arr) - 1
    contagem_comparacoes = 0

    while esquerda <= direita and alvo >= arr[esquerda] and alvo <= arr[direita]:
        contagem_comparacoes += 1
        posicao_estimada = esquerda + int(((direita - esquerda) * (alvo - arr[esquerda])) / (arr[direita] - arr[esquerda]))

        if arr[posicao_estimada] == alvo:
            return posicao_estimada, contagem_comparacoes
        if arr[posicao_estimada] < alvo:
            esquerda = posicao_estimada + 1
        else:
            direita = posicao_estimada - 1

    return -1, contagem_comparacoes

# Exemplo de uso
arr_exemplo = [2, 4, 6, 8, 10, 12, 14, 16]
alvo_busca = 4
indice, comparacoes = busca_interpolada(arr_exemplo, alvo_busca)

if indice != -1:
    print(f"Alvo encontrado na posição {indice} com {comparacoes} comparações.")
else:
    print("Alvo não encontrado.")
