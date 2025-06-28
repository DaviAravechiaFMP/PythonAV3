from Dif import easy
from random import randint

def play(nivelDif):
    import os
    from load import loading
    from random import randint
    dicePlayer1 = 0
    dicePlayer2 = 0
    match nivelDif:
        case 'F':
            path = easy()
            while True:
                for i in range(2):
                    print(f'''
                        Gire o dado jogador {i+1}:
                        Pressione Enter para girar
                        ''')
                    input()
                    valorDado = randint(1,6)  
                    print(f'''
                        O valor do dado deu:
                        {valorDado}
                        Pressione enter para continuar
                        ''')
                    if path[19] == 1 or path[19] == 2:
                        print('O jogo acabou, o jogador', path[19], 'ganhou!')
                        return
                    if i == 0:
                        dicePlayer1 += valorDado
                        cont = 0
                        if 1 in path:
                            path[path.index(1)] = '_'
                        path.insert(dicePlayer1 -1, 1)
                        print(' '.join(str(p) for p in path)) #entender como funciona, solução do chat
                        # print(' '.join(path))
                    
                    else:
                        dicePlayer2 += valorDado
                        if 2 in path:
                            path[path.index(2)] = '_'
                        path.insert(dicePlayer2 -1, 2)
                        print(' '.join(str(p) for p in path)) #entender como funciona, solução do chat
                        # print(' '.join(path))
                    input()
                    os.system('cls')