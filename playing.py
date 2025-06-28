from Dif import easy, mid
from random import randint

def play(nivelDif):
    import os
    from load import loading
    from random import randint
    import time
    # from verifyCase import verify
    dicePlayer1 = 0
    dicePlayer2 = 0
    match nivelDif:
        case 'F':
            path = easy()
        case 'M':
            path = mid()
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
            valorDado = randint(1,3)  
            print(f'''
                O valor do dado deu:
                {valorDado}
                Pressione enter para continuar
                ''')
            if i == 0:
                dicePlayer1 += valorDado
                housesToMove = dicePlayer1
                for i in range(housesToMove - valorDado, housesToMove + 1):    
                    if path[i] == 2 and 2 in path:
                        path[i] = '∆'
                        path[i - 1] = '_'
                    else:
                        path[i] = 1
                        if path[i-1] == '∆': 
                            path[i-1] = 2    
                        elif path[i - 1] != '∆':
                            path[i-1 ] = '_'
                        time.sleep(0.5)
                    os.system('cls')
                    print(' '.join(str(p) for p in path)) #entender como funciona, solução do chat
                # print(' '.join(str(p) for p in path)) #entender como funciona, solução do chat
                # print(' '.join(path))
            
            else:
                dicePlayer2 += valorDado
                housesToMove = dicePlayer2

                # path[dicePlayer2] = 2
                for i in range(housesToMove - valorDado, housesToMove + 1):
                    if path[i] == 1:
                        path[i] = '∆'
                        path[i - 1] = '_'
                    else:
                        path[i] = 2
                        if path[i-1] == '∆': 
                            path[i-1] = 1 
                        elif path[i - 1] != '∆':
                            path[i-1 ] = '_'
                    time.sleep(0.5)
                    os.system('cls')
                    print(' '.join(str(p) for p in path)) #entender como funciona, solução do chat
                # if dicePlayer1+ valorDado >= pathOrigin -1 or dicePlayer2 + valorDado >= pathOrigin -1:
                if path[pathOrigin -1] == 1 or path[pathOrigin -1] == 2:
                    if i == 0:
                        winner = 'Jogador 1'
                    else:
                        winner = 'Jogador 2'
                    print(f'O jogo acabou o {winner} ganhou!')
                # print(' '.join(path))
            input()
            os.system('cls')