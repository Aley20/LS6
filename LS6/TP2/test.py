def petit(liste):
    res=0
    for i in range (1,len(liste)-1):
        for j in range (1,len(liste[i])-1):
            if liste[i][j]>liste[i+1][j] and liste[i][j]>liste[i-1][j] and liste[i][j]>liste[i][j-1] and liste[i][j]>liste[i][j+1]:
                res+=1
    return res

M=[[1,4,9,1,4],[4,8,1,2,5],[4,1,3,4,6],[5,0,4,7,6],[2,4,9,1,5]]
print("petit -> ",petit(M))

def multiple (n) :
    return [x for x in range(n) if x%5==0 or x%7==0]

print("multiple -> ", multiple(15))

def multiple_idx(l):
    return [x for x in l if x%5==0 or x%7==0]

print("multiple_idx -> ", multiple_idx([1,2,4,5,7,8,9,14,15]))

def zipping (l,m):
    return list(zip(l,m))

print("zipping -> ",zipping([1,2,3],[1,2,3]))

def transpose (m) :
    return [[x[i] for x in m] for i in range(len(m[0]))]

print("transpose -> ",transpose([[1,2,3],[4,5,6]]))

def tens(n) :
    return [[x*10+i for i in range(10)] for x in range(n)]

print ("tens -> ",tens(2))

def flatten(ll):
    res=[]
    for i in ll:
       if isinstance(i,list):
           res.extend(flatten(i))
       else:
          res.append(i)
    return res

print ("flatten -> ",flatten([[1,2], [3,4,5], [-6]]))

def myqs(L):
    if len(L) <= 1: return L
    pivot = L[0]
    return myqs([x for x in L[1:] if x< pivot ]) + [pivot] + myqs([x for x in L[1:] if x>=pivot])

print("myqs -> ",myqs([1, 7, 4, 1, 10, 9, -2]))


def without_e(mot) :
    return [x for x in mot if 'e' not in x]

l=["bonjour","hello","hey","bien","ok"]
print("without_e -> ",without_e(l))

def nstutter(mot):
    words=mot.split()
    debut=[]
    prive=''
    for i in range(1,len(words)) :
        if words[i]!=words[i-1] and prive!=words[i-1]:
            debut.append(words[i-1])
        else :
            debut.append(words[i-1])
            prive=debut.pop()
            

    return ' '.join(debut)

text = "hello world world is beautiful beautiful ."
print("nstutter ->",nstutter(text)) 

def prefixes(w, long_max) :
    return [w[:i] for i in  range(1,min(len(w),long_max)+1) ]

print (prefixes("bonjour",3))

def cube_prefixes(w):
    for i in range(1, len(w)):
        prefix = w[:i]
        cube = str(int(prefix) ** 3)
        if cube == w[:len(cube)]:
            return True
    return False

print("813 -> ",cube_prefixes("813"))
print("2 -> ",cube_prefixes("512371"))
print("2 -> ",cube_prefixes("27"))
print("2 -> ",cube_prefixes("121")) 
