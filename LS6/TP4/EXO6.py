def parserG(nomfich) :
    f=open(nomfich,'r') 

    oriente = False
 
    ligne=f.readline()
   
    if ligne.startswith("Graphe") :
        if "oriente" in ligne:
            oriente=True
            
        if "non-oriente" in ligne:
            oriente=False
            
        ligne=f.readline()

        if ligne.startswith("%"):
            ligne=f.readline()
             
            if  ligne.startswith("Sommets"):
                ligne=f.readline()
                ligne=f.readline()
            else :
                ligne=f.readline()
                print("pas de sommet")
                return

            if ligne.startswith("Transitions") :
                if oriente: 
                    print ("O") 
                else: 
                    print("NO")
            else :
                    print("pas de transitions")

    else :
        print("erreur de syntaxe")





