# EX1
import string
def Chaine(s,c):
    return c.lower() in s

print(Chaine('toto','O'))

# EX2
def afficheListe(L):
    L.reverse()
    return L
    

print(afficheListe([56,7,4,8,23,89,101,78]))

# EX3
def sous_liste(L,k):
    return [x for x in L if L.index(x)%k==0]

print(sous_liste([56,7,4,8,23,89,101,78],3))

# EX4
def minP(L):
    return min([x for x in L if L.index(x)%2==0])

print(minP(afficheListe([56,7,4,8,23,89,101,78])))

# EX5
def TriLong(L):
    return sorted(L, key=len, reverse=True)

print(TriLong(['bip','toto','azerty','blablabla','a','alo']))

# EX6
def LireCompter():
    fin=False
    list=[]
    print("Veuillez saisir des chaines : ")

    while not fin:
        v=input()
           
        if v=='fin':
            fin=True
        
        else :
            list.append(v)

        dic={}
        
        for i in list:
            for j in i:
                if j not in dic:
                    dic[i]=list.count(i)
                
    return dic

#print(LireCompter())

# EX7
def NbLignes(nom):
    count=0
    f=open(nom,'r')
    lignes=f.readlines()
    for ligne in lignes:
        if ligne.startswith("bip"):
            count+=1
    return count

print(NbLignes('toto.txt'))

# EX9

from random import *
def newListe(n):
    return [randint(1,13) for x in range(n)]
print(newListe(6))

def ChoixOrdi(L):
    i=randint(0,1)
    if i==0:
        return "gauche"
    else :
        return "droite"

print(ChoixOrdi(newListe(6)))

def QuiGagne(L1,L2):
    res1=0
    res2=0
    for i in L1:
        res1+=i
    for i in L2:
        res2+=i

    if res1>res2:
        print("Joueur 1 vainqueur ")
    elif res1<res2:
        print("Joueur 2 vainqueur")
    else :
        print("Match nulle")

QuiGagne([0,4],[0,1])

def Cartes(n):
    L=newListe(n)
    tour=False # False -> Joueur , True -> ordinateur
    LJ=[]
    LO=[]

    while L!=[] :
        print (L)
        if not tour:
            try :
                
                v=input("Veuillez choisir une extremite : (droite)(gauche)")
                if v=='droite' :
                    LJ.append(L[-1])
                    L.remove(L[-1])
                    tour=True
                elif v=='gauche':
                    LJ.append(L[0])
                    L.remove(L[0])
                    tour=True
                else :
                    print("Veuillez choisir entre (droite) et (gauche) !")
               
            except KeyboardInterrupt :
                print("Parti fini")
                break
                
                
            
        else :
            tour=False
            v=ChoixOrdi(L)
            if v=='droite':
                LO.append(L[-1])
                L.remove(L[-1])
            else :
                LO.append(L[0])
                L.remove(L[0])
    
    print("Parti fini, plus de cartes")
    QuiGagne(LJ,LO)

Cartes(3)


        








