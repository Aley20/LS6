# 1
def without_e (l) :
    res=[]
    for x in l:
        if 'e' not in x:
            res.append(x)
    return res

l=["bonjour","hello","hey","bien","ok"]
print("1 -> ",without_e(l))

# 2
def nstutter(text):
    words=text.split()
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
print("2 ->",nstutter(text)) 
