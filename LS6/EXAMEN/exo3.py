#1
import sys
def getopts():
    d={"l":False, "t":False}
    for arg in sys.argv[1:]:
        if arg=="-l":
            d["l"]=True
        elif arg=="-t":
            d["t"]=True
    return d
print(getopts())

#2
def getfiles():
    l=[]
    for arg in sys.argv[2:]:
        if arg!='-':
            l.append(arg)
        else:
            l.append('-')

    return l

print(getfiles())

#3
def analyse(line):
    words=line.split() # transforme chaine en liste
    nb_word=len(words)
    cpt=0              # ou cpt=sum(words[i] for i in range(nb_word))
    for i in range (nb_word): 
        cpt+=len(words[i])
    return nb_word,cpt

print(analyse("hello ok o"))

#4