class FIFO:
    def __init__(self):
        self.Tin=[]
        self.Tout=[]
        self.taille=0
    
    def ajout(self,x):
        self.Tin.append(x)
        self.taille+=1
    
    
    def supprime(self):
        if self.taille==0 :
            raise IndexError("Impossible de depiler !") 
        if len(self.Tout)!=0:
            self.Tout.pop()
            self.taille-=1
        else :
            for i in range(len(self.Tin)):
                self.Tout.append(i)
            self.Tin=[]
            self.Tout.pop()
            self.taille-=1

    def tete(self):
        if self.taille==0:
            raise IndexError("Impossible de depiler !") 
        if len(self.Tout)!=0:
            return self.Tout[len(self.Tout)-1]
        else : 
            for i in range(len(self.Tin)):
                self.Tout.append(i)
            self.Tin=[]
            return self.Tout[len(self.Tout)-1]



