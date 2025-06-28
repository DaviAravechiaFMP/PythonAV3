def inicialization(nivelDif):
    import os
    from load import loading
    print(f'''
{'='*50}
Bem vindo!!
Deseja começar o jogo?
Para começarmos selecione a dificuldade desejada:
Fácil - F
Médio - M
Díficil D
{'='*50}
''')
    valoresValidos = ['F', 'M', 'D']
    nivelDif = input().upper()

    while True:
        # if nivelDif == 'F' or nivelDif == 'M' or nivelDif == 'D':
        if nivelDif in valoresValidos:
                    break
        else:
            print('Insira um valor válido')
            nivelDif = input().upper()
    os.system('cls')
    # loading()
    os.system('cls')
    return(nivelDif)