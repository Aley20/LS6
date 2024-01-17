# 1
def multiple(n) :
    return [x for x in range(n) if x%5 == 0 or x%7 ==0]

print("1 -> ",multiple(10))

# 2
def multiple_idx(l):
    return [x for x in l if x%5==0 or x%7==0]

print("2 -> ",[0,5,7,6,8,9,0,5,3,7,15])
print ("2 -> ",multiple_idx([0,5,7,6,8,9,0,5,3,7,15]))

# 3
def zipping(l,m):
    return list(zip(l,m))

L=[1,2,3,4]
L1=[1,2,3,4]
print("3 -> ",zipping(L,L1))

# 4
def transpose (m) :
    return [[x[i] for x in m] for i in range (len(m[0]))]

print("4 -> ",transpose([[1,2,3],[4,5,6]]))

# 5 
def tens(n) :
    return [[x+10*i for x in range (10)] for i in range(n)]

print("5 -> ",tens(3))

# 6
def flatten(ll) :
    res=[]
    for x in ll :
        if isinstance(x,list):
            res.extend(flatten(x))
        else :
            res.append(x)
    return res

print("6 -> ",flatten([[1,2], [3,4,5], [-6]]))

# 7
def myqs(L):
    if len(L) <= 1: return L
    pivot = L[0]
    return myqs([x for x in L[1:] if x < pivot]) + [pivot] + myqs([x for x in L[1:] if x>=pivot])

import random
print("7 -> ",myqs([1, 7, 4, 1, 10, 9, -2]))
l=list(range(10000))
random.shuffle(l)
L2=l[:]
print("sort ->",l.sort())
print("myqs ->",myqs(L2))

