# 1
def list_to_dict(l) :
    return {i: l[i] for i in range(len(l))}

print(list_to_dict(["petit", "klein", "small"]))

# 1.1
def list_to_dict2(l) :
    return dict(enumerate(l))

print(list_to_dict2(["petit", "klein", "small"]))

# 2
def chars(w):
    res=dict()
    for i in w:
        if i not in res.keys():
            res[i]=w.count(i)
            
    return res 

# 2.2
def chars_1(w):
    res={c:0 for c in w}
    for c in w:
        res[c]+=1          
    return res 

def chars_2(w):
    res=dict()
    for x in w:
        if x in res:
            res[x]+=1
        else :
            res[x]=1
    return res

def print_dict(d) :
    for (k, v) in d.items():
        print(k,v)  

print_dict(chars("aacababbcc"))
print()
print_dict(chars_1("aacababbcc"))
print()
print_dict(chars_2("aacababbcc"))

# 3
def merge(d1, d2):
    res=dict()
    for (k1, v1) in d1.items():
        for (k2, v2) in d2.items():
            if k1==k2 :
                res[k1]=(v1,v2)

    return res

d1 = {'r': 0.56, 't': 0.78, 'i': 0.23, 'u': 0.35}
d2 = {'i': 5, 'v': 89, 'p': 65, 't': 21, 'b': 55}
print(merge(d1, d2))

# 4
def inverse(d):
    res=dict()
    for (k, v) in d.items():
           res[v]=k
    return res

print(d1)
print("inverse ",inverse(d1))
print(inverse(d2))

