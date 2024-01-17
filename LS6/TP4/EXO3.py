#!/usr/bin/env python3
import string
import sys
# -*- coding: utf-8 -*-

def frequence (nomfich,n=5) : # valeur par défaut
    f=open(nomfich,'r')
    text=f.read()
    text=text.lower()
    mots=text.split()
    dico={}
    for mot in mots:
        m=mot.strip(string.punctuation)
        if m.isalpha():
            if m in dico.keys() :
                dico[m]+=1
            else :
                dico[m]=1  

    res={}

    for (k,v) in dico.items(): 
        if len(k)>n:
            res[k]=v
    

    mot_trie=sorted(res.items(),key=lambda x:x[1],reverse=True)

    return mot_trie[:5]

if __name__=='__main__':
    nomfich=sys.argv[1]
    resultat=frequence(nomfich)
    print(resultat)