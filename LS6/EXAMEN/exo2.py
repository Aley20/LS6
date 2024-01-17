#1
def ok(f):
    n=len(f)
    for x in f:
        if x<0 or x>=n:
            return False
    return True

l=[0,1,2,3]
l1=[3,3,4,2]
print("ok([0,1,2,3]) -> ",ok(l))
print("ok([5,3,4]) -> ",ok(l1)) 

#2
def codomain(f):
    return set(f)

print("codomain[5,3,4] -> ",codomain(l1))

ll=[3,3,3,0]
#3 
def compose(f,g):
    n=len(f)
    h=[0]*n
    for i in range(n):
        h[i]=f[g[i]]
    return h

print("compose -> ",compose(l,ll))

#4
def list2dict(f):
    return {i:f[i] for i in range(len(f))}

p=list2dict(ll)
print("dict([3,3,3,0]) -> ",p)

#5
def dict2list(f):
    l=[]
    for (k,v) in f.items():
        l=l+[v]

    return l

print("dict2list() -> ",dict2list(p))

#6
def one2one(f):
    values = set()
    for x in f:
        if x in values:
            return False
        values.add(x)
    return True

print("one2one() -> ",one2one(l1))  
#7
def inverse(f):
    n = len(f)
    if not one2one(f):
        return None
    d={f[i]:i for i in range(n)}
    return [d[i] for i in range (n)]

s=[2,3,1,0]
print(s)
print("inverse ",inverse(s))  

