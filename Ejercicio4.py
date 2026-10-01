#La Organización de Springfield

def orden (L:list, exp=False)->list:
    list_ord=sorted(L)
    if exp is True:
        return list_ord [::-1]
    else:
        return list_ord


    