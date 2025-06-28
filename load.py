def loading():
    import time
    import os
    from info import information
    loadingList = ['['] + [' ']* 10 + [']']
    print('Loading...')
    print(''.join(loadingList))
    information()
    for i in range(1,len(loadingList)):
        loadingList.insert(i,'*')
        loadingList.pop(-2)
        time.sleep(0.5)
        os.system('cls')
        print('Carregando...')
        print(''.join(loadingList))
        information()
    input('Pressione Enter para continuar')