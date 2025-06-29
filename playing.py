from Dif import easy, mid, hard
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
        case 'D':
            path = hard()
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
            if i == 0:
                dicePlayer1 += valorDado
                housesToMove = dicePlayer1
                for i in range(housesToMove - valorDado, housesToMove + 1):    
                    if path[i] == 2 and 2 in path:
                        path[i] = '∆'
                        path[i - 1] = '_'
                    elif path[i] == '∆':
                        continue
                    else:
                        path[i] = 1
                        if path[i-1] == '∆': 
                            path[i-1] = 2    
                        elif path[i - 1] != '∆':
                            path[i-1] = '_'
                        time.sleep(0.5)
                        os.system('cls')
                        print(' '.join(str(p) for p in path)) #entender como funciona, solução do chat
                    if path[-1] == 1:
                        print('Jogador 1 venceu!')
                        input('Pressione Enter para continuar')
                        return
                # print(' '.join(str(p) for p in path)) #entender como funciona, solução do chat
                # print(' '.join(path))
            
            else:
                dicePlayer2 += valorDado
                housesToMove = dicePlayer2

                # path[dicePlayer2] = 2
                for i in range(housesToMove - valorDado, housesToMove + 1):
                    if path[i] == 1 and 1 in path:
                        path[i] = '∆'
                        path[i - 1] = '_'
                    elif path[i] == '∆':
                        continue
                    else:
                        path[i] = 2
                        if path[i-1] == '∆': 
                            path[i-1] = 1 
                        elif path[i - 1] != '∆':
                            path[i-1 ] = '_'
                    time.sleep(0.5)
                    os.system('cls')
                    print(' '.join(str(p) for p in path)) #entender como funciona, solução do chat
                    if path[-1] == 2:
                        print('Jogador 2 venceu!')
                        input('Pressione Enter para continuar')
                        return
                # if dicePlayer1+ valorDado >= pathOrigin -1 or dicePlayer2 + valorDado >= pathOrigin -1:

                # print(' '.join(path))
            input()
            os.system('cls')