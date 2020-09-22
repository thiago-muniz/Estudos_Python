def spam():
    print(eggs) #ERRO!
    eggs = 'spam local'


eggs = 'global'
spam()