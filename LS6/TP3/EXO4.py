# 1
def init_table(n):
    return [None for i in range(n)]

print("**************** Question 1 ********************")
print(init_table(5))

# 2 
def add_elt(x,n,t):
    for i in range(len(t)):
        if t[i]==None :
            t[i]=x
            return True

    return False

l=(init_table(5))
print("**************** Question 2 ********************")
print(add_elt(1,5,l))
print(add_elt(2,5,l))
print(add_elt(3,5,l))
print(add_elt(4,5,l))
print(add_elt(5,5,l))
print(add_elt(2,5,l))

# 3
def in_table(x,n,t):
    for i in t:
        if i==x:
            return True
    return False

print("**************** Question 3 ********************")
print(in_table(5,5,[1,2,3,4,5]))
print(in_table(5,5,[1,2,3,4]))

# 4
def test_hash(n,l):
    table=init_table(n)
    for i in l:
        if add_elt(i,n,table)==False and in_table(i,n,table)==False:
            return False
    return True

print("**************** Question 4 ********************")
print (test_hash(5,[1,2,3,4,4]))
print (test_hash(3,[1,2,3,4,4]))

# 5 
def test_set(l):
    res={}
    res={x for x in l}
    for i in l:
        if i not in res:
            return False
    return True

print("**************** Question 5 ********************")
print(test_set([1,2,3]))

# 6
import random
def hash_benchmark(k, m, n):
    l=[random.randint(0,m) for x in range(k)]
    from time import process_time
    tps1 = process_time()
    test_hash(n, l)
    res1=process_time()-tps1
    tps2 = process_time()
    test_set(l)
    res2=process_time()-tps2
    print("test_hash(n,l) -> ",res1)
    print("test_set(l) -> ",res2)

print("**************** Question 6 ********************")
print(hash_benchmark(5,10,3))

# 7
def suppr(x,n,t):
    if in_table(x,n,t) :
        del(t[t.index(x)])
    else :
        return

print("**************** Question 7 ********************")
t=[3,4,5,6,7]
print(suppr(5,5,t))
print(t)
print(suppr(0,5,t))
print(t)


