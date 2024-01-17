class Pile :

    def __init__(self) : # c’est le constructeur !
        self.T=[]
        self.taille=0
    
    def empiler(self,x) :
        self.T.append(x)
        self.taille+=1

    def depiler(self) :
        if self.taille==0 :
            raise IndexError("Impossible de depiler une pile vide !") 
        self.T.pop()
        self.taille-=1
    
    def tete(self) :
        if self.taille==0 :
            raise IndexError("Une pile vide n’a pas de tete !") 
        return self.T[self.taille-1]
    
    def estvide(self) :
        return self.taille==0
    
    def __str__(self) :
       return f'Pile : ({self.taille}) | '+str(self.T)[1:-1] 
    # f permet de remlacer self.taille par sa valeur 
    # [1:-1] enlève 1er et derniere valeur
    # pour tester print(v)