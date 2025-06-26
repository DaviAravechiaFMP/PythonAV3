def loading():
    import time
    import os
    loadingList = ['['] + [' ']* 10 + [']']
    print('Loading...')
    for i in range(1,len(loadingList)):
        loadingList.insert(i,'*')
        loadingList.pop(-2)
        time.sleep(0.5)
        os.system('cls')
        print('Carregando...')
        print(''.join(loadingList))