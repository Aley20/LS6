# 1
def same_elements(l1, l2):
    return set(l1) == set(l2)
    

l1=[1,2,3]
l2=[3,2,1]
print(same_elements(l1,l2))

# 2
def letters():
    l=input("Entrez une phrase !")
    return set(x.lower() for x in l if x.lower()>='a' and x.lower()<='z')

# 3
def to_list(s):
    return list(s)
print(to_list({4,5,1,2}))

def to_ens(l):
    return set(l)
print(to_ens([4,5,1,2]))

# 4
def even(s):
    return {x for x in s if x%2==0}

print(even({2,4,5,6,8,5}))