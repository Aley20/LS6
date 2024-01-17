#!/usr/bin/env python3
# EX7
def NbLignes(nom):
    count=0
    f=open(nom,'r')
    lignes=f.readlines()
    for ligne in lignes:
        if ligne.startswith("bip"):
            count+=1
    return count

# EX8
import sys
if __name__ == '__main__':
    nomfich=sys.argv[1]
    res = NbLignes(nomfich)
    print(res)