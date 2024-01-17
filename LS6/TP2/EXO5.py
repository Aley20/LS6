# 1
def prefixes(w, long_max):
    #return [w[:i] for i in range(1,min(len(w),long_max)+1)] 
    res=[]
    for i in range(1,long_max+1):
        res.append(w[:i])

    return res
    # la fonction min() est utilisée pour s'assurer que la taille 
    # du préfixe ne dépasse pas long_max, même si la longueur du mot w 
    # est supérieure à long_max.

print("1 -> ",prefixes("Bonjour", 4))

# 2
def cube_prefixes(w):
    for i in range(1, len(w)):
        prefix = w[:i]
        cube = str(int(prefix) ** 3)
        if cube == w[:len(cube)]:
            return True
    return False

print("2 -> ",cube_prefixes("813"))
print("2 -> ",cube_prefixes("512371"))
print("2 -> ",cube_prefixes("27"))
print("2 -> ",cube_prefixes("121")) 

# 3

def no_cube(w) :
    for i in range (len(w)):
        if cube_prefixes (w[i:]) :
            return True

    return False
