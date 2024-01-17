# 1
import re

def filtre1(nomfich):
    f=open(nomfich,'r')
    for ligne in f:
        mots = re.findall(r'\b\w{8,12}\b', ligne)
        if mots and ligne.startswith(mots[0]):
            print(ligne.strip())


def ffiltre1(f):
    with open(f,'r') as fr:
        p=re.compile(r'\w{8,12}\b') # \b limite de mot 
                                    # \w mot
        for l in fr:
            if p.match(l):
                print(l)
print("EXO1 : ") 
ffiltre1("toto.txt")

# 2
def filtre2(nomfich):
    f=open(nomfich,'r')
    for ligne in f:
        if "toto" in ligne:
            print(ligne.strip())


def ffiltre2(f):
    with open(f,'r') as fr:
        p=re.compile(r'\btoto\b') # \b limite de mot 
                                   
        for l in fr:
            if p.search(l):
                print(l) 

print("EXO2 : ") 
ffiltre2("toto.txt")

# 3
def filtre3(nomfich):
    f=open(nomfich,'r')
    for ligne in f:
        if ligne.count("toto")>=3 in ligne:
            print(ligne.strip())

def ffiltre3(f):
    with open(f,'r') as fr:
        p=re.compile(r'\btoto\b.*\btoto\b.*\btoto\b') 
        for l in fr:
            if p.search(l):
                print(l) 

print("EXO3 : ") 
ffiltre3("toto.txt")

# 4
def ffiltre4(f):
    with open(f,'r') as fr:
        p=re.compile(r'.*\b([a-z]+)\b.*\b\1\b.*\b\1\b')  
        # -----[a-z]------[a-z]------[a-z]----- (.*-> -------)

        for l in fr:
            if p.match(l):
                print(l) 

print("EXO4 : ") 
ffiltre4("toto.txt")