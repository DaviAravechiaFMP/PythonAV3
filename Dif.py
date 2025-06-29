def easy():
    import os
    path = ['∆']
    path.extend('_'*19)

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
    path = ['∆']
    path.extend('_'*39)

    # for i in range(randint(1, 3)):
    
    print(F'''

Esse é o caminho que vocês devem finalizar:
          
{' '.join(path)}
''')
    input('Pressione Enter para continuar')
    os.system('cls')
    
    return(path)

def hard():
    import os
    from random import randint
    path = ['∆']
    path.extend('_'*79)

    # for i in range(randint(1, 3)):
    
    print(F'''

Esse é o caminho que vocês devem finalizar:
          
{' '.join(path)}
''')
    input('Pressione Enter para continuar')
    os.system('cls')
    
    return(path)