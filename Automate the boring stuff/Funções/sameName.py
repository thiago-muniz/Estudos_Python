def spam():
    eggs = 'spam local'
    print(eggs) #exibe 'spam local'


def bacon():
    eggs = 'bacon local'
    print(eggs) #exibe 'bacon local'
    spam()
    print(eggs) #exibe 'spam local'

eggs = 'global'
bacon()
print(eggs) #exibe 'global'
