import string
def exo4(nomdico, fichtexte):
    res=open(nomdico,'r').read()
    fp=open(fichtexte,'r')
    mots=fp.read().split()
    mot_corrige=[]

    nom=fichtexte+'_corrige'      #on crée une variable de type string
    
    with open(nom,'w') as f:
        for mot in mots:
            p=mot.strip(string.punctuation)
            if mot.isalpha() and not any(p.lower() in ligne.lower() for ligne in res.splitlines()): #transforme fich en list
            # parcours chaque ligne du dictionnaire, met le mot à vérifier en minuscules (lower()), et cherche si le mot se trouve dans la ligne

                print("okk")
                punc = ' '.join(c for c in mot[len(p):] if c in string.punctuation)
                f.write('***' + p + '***' + punc + ' ')
                mot_corrige.append(p)
            else:
                f.write(mot + "  ")
    print ("Mot abs: ",mot_corrige)           
                
