def busca_fibonacci(arr, alvo):
    tamanho = len(arr)
    fib_2 = 0
    fib_1 = 1
    fib_num = fib_2 + fib_1
    total_comparacoes = 0

    while fib_num < tamanho:
        fib_2, fib_1 = fib_1, fib_num
        fib_num = fib_2 + fib_1

    deslocamento = -1

    while fib_num > 1:
        total_comparacoes += 1
        indice = min(deslocamento + fib_2, tamanho - 1)

        if arr[indice] < alvo:
            fib_num, fib_1, fib_2 = fib_1, fib_2, fib_num - fib_1
            deslocamento = indice
        elif arr[indice] > alvo:
            fib_num, fib_1, fib_2 = fib_2, fib_1 - fib_2, fib_2 - fib_1
        else:
            return indice, total_comparacoes

    if fib_1 and deslocamento + 1 < tamanho and arr[deslocamento + 1] == alvo:
        total_comparacoes += 1
        return deslocamento + 1, total_comparacoes
    return -1, total_comparacoes
