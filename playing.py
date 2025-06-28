from Dif import easy
from random import randint

def play(nivelDif):
    import os
    from load import loading
    from random import randint
    # from verifyCase import verify
    dicePlayer1 = 0
    dicePlayer2 = 0
    match nivelDif:
        case 'F':
            path = easy()
            pathOrigin = len(path)
            while True:
                for i in range(2):
                    if len(path) > pathOrigin:
                        path.pop()
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
                    if dicePlayer1+ valorDado >= 19 or dicePlayer2 + valorDado >= 19:
                        if i == 0:
                            winner = 'Jogador 2'
                        else:
                            winner = 'Jogador 1'
                        print(f'O jogo acabou o {winner} ganhou!')
                        return
                    if i == 0:
                        dicePlayer1 += valorDado
                        
                        if 1 in path:
                            path[path.index(1)] = '_'
                        elif '∆' in path:
                            path[path.index('∆')] = '_'
                        if 2 in path:
                            if dicePlayer1 == path.index(2):
                                path[dicePlayer2] = '∆'
                            else:
                                path[dicePlayer1] = 1
                        else:
                            path[dicePlayer1] = 1
                        print(' '.join(str(p) for p in path)) #entender como funciona, solução do chat
                        # print(' '.join(path))
                    
                    else:
                        dicePlayer2 += valorDado
                        if 2 in path:
                            path[path.index(2)] = '_'
                        # elif dicePlayer2 == dicePlayer1:
                        #     path[dicePlayer1] = '∆'
                        elif '∆' in path:
                            path[path.index('∆')] = '_'
                        if dicePlayer2 == path.index(1):
                            path[dicePlayer1] = '∆'
                        else:
                            path[dicePlayer2] = 2
                        print(' '.join(str(p) for p in path)) #entender como funciona, solução do chat
                        # print(' '.join(path))
                    input()
                    os.system('cls')