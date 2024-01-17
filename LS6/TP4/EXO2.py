#!/usr/bin/env python3
import string
import sys
def frequence (nomfich) :
    f=open(nomfich,'r')
    text=f.read()
    text=text.lower()
    mots=text.split() # transforme la ligne en liste 
    dico={}
    for mot in mots:
        m=mot.strip(string.punctuation)
        if m.isalpha():
            if m in dico.keys() :
                dico[m]+=1
            else :
                dico[m]=1  
    mot_trie=sorted(dico.items(),key=lambda x:x[1],reverse=True)
    return mot_trie[:5]

if __name__=='__main__':
    nomfich=sys.argv[1]
    resultat=frequence(nomfich)
    print(resultat)


import string
def ex(nomfich):
    f=open(nomfich,'r')
    text=f.read()
    text=text.lower()
    mots=text.split() # transforme la ligne en liste
    dico={}
    for mot in mots:
        m=mot.strip(string.punctuation)
        if m.isalpha():
            if m in dico.keys() :
                dico[m]+=1
            else :
                dico[m]=1
    mot_trie=sorted(dico.items(),key=lambda x:x[1],reverse=True)
    return mot_trie[:5]




