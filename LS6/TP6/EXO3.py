import re
# 1
def parse_line(s):
    p=re.compile(r'(\d{4}),(\d+),(\d+),(.+)') # Définir l'expression rationnelle pour extraire les informations
    match = p.fullmatch(s)  
    if match :
        annee = int(match.group(1))
        nombre = int(match.group(2))
        idn = int(match.group(3))
        Prenom = match.group(4)
        return (annee, nombre, idn, Prenom)
    else :
        return 
   
print('************* Question 1 **************')  
print(parse_line('2022,1234,123,John'),'\n')
print(parse_line('202,1234,123,John'))


# 2
def parse_line(s,motif):
    m=motif.fullmatch(s)
    if m:
        return (int(m.group(1)),int(m.group(2)),int(m.group(3)),m.group(4))
    
def parse_file(path):
    m=re.compile(r'(\d{4}),(\d+),(\d+),(.+)')
    d = dict()
    with open(path, 'r') as fin:
        for l in fin:
            laux=l.strip()
            res=parse_line(laux,m)
            if res :
                d[res[0],res[3]]=d.get((res[0],res[3]),0)+res[1]
    return d

print('************* Question 2 **************') 
print(parse_file('toto3.txt'),'\n')
#print(parse_file('prenoms.txt'),'\n')

# 3 
def name_frequency(d):
    res={}
    for (x,n),v in d.items():
        res[n]=res.get(n,0)+v
        
    return res

print('************* Question 3 **************') 
d = parse_file("toto3.txt")
name_freq = name_frequency(d)
print(name_freq)
print(name_freq["Djemaa"])

# 4
def popular_name(fname,n):
    fr=name_frequency(parse_file(fname))
    sfr = sorted([(v,prenom) for (prenom,v) in fr.items()], reverse=True)
    # Affiche les n prénoms les plus utilisés
    for (v,prenom) in sfr[:n]:
        print(prenom,v)

print('************* Question 4 **************') 
print(popular_name('prenoms.txt',5))
print('\n')

# 4.1
# 1
def is_square(w):
    w=w.lower()
    return re.fullmatch(r'(.+)\1',w) is not None

p=name_frequency(parse_file('prenoms.txt'))
print('************* Exercice 4 **************') 
print('************* Question 1 **************') 
print("carre : ",len([(prenom,nb) for prenom,nb in p.items() if is_square(prenom)]))


# 2
def contains_square(w):
    w=w.lower()
    return re.search(r"(..+)\1",w) is not None

print('************* Question 2 **************') 
print("carre de longueur min 4 : ",len([(prenom,nb) for prenom,nb in p.items() if contains_square(prenom)]))

# 3 
# 5 fois la meme lettre 
def quest3(w):
    w=w.lower() 
    return  re.search(r"(\w).*\1.*\1.*\1.*\1",w) is not None

print('************* Question 3 **************') 
print("5 fois la meme lettre : ",len([(prenom,nb) for prenom,nb in p.items() if quest3(prenom)]))

# 4
# 4 voyelle consécutive 
def quest4(w):
    w=w.lower() 
    return  re.search(r"[aeiouy]{4,}",w) is not None

print('************* Question 3 **************') 
print("5 fois la meme lettre : ",len([(prenom,nb) for prenom,nb in p.items() if quest4(prenom)]))


# 5
# 4 consonne consécutive 
def quest5(w):
    w=w.lower() 
    return  re.search(r"[bcdfghgklmnpqrstvwxz]{4,}",w) is not None

print('************* Question 3 **************') 
print("5 fois la meme lettre : ",len([(prenom,nb) for prenom,nb in p.items() if quest5(prenom)]))

# 6
def quest6(w):
    w=w.lower() 
    return  re.search(r"(.+)[bcdfghgklmnpqrstvwxz]{4,}",w) is not None

print('************* Question 3 **************') 
print("5 fois la meme lettre : ",len([(prenom,nb) for prenom,nb in p.items() if quest6(prenom)]))