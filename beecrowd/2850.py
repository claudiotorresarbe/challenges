while True:

    try:

        n = input()

        if n == 'esquerda':
            print('ingles')
        elif n == 'direita':
            print('frances')
        elif n == 'nenhuma':
            print('portugues')
        elif n == 'as duas':
            print('caiu')

    except:

        break