def deslocar(letra,posicao):

    a = ord(letra)
    b = a + posicao
    result = chr(b)

    return result

n = int(input())

if 1 <= n <= 1*10**4:

    for x in range(n):

        m = input()

        if 1 <= len(m) <= 1*10**3:

            primeira_passada = [deslocar(x,3) if x.isalpha() else x for x in m]
            segunda_passada = primeira_passada[::-1]
            tamanho = int(len(segunda_passada)/2)
            metade_a = segunda_passada[0:tamanho]
            metade_b = segunda_passada[tamanho::]
            terceira_passada = [deslocar(x,-1) for x in metade_b]
            ultimo = metade_a+terceira_passada
            print(''.join([x for x in ultimo]))