def easy():
    import os
    path = []
    path.extend('_'*20)

    print(F'''

Esse é o caminho que vocês devem finalizar:
          
{' '.join(path)}
''')
    input('Pressione Enter para continuar')
    os.system('cls')
    
    return(path)

def mid():
    import os
    from random import randint
    path = []
    path.extend('_'*40)

    # for i in range(randint(1, 3)):
    
    print(F'''

Esse é o caminho que vocês devem finalizar:
          
{' '.join(path)}
''')
    input('Pressione Enter para continuar')
    os.system('cls')
    
    return(path)