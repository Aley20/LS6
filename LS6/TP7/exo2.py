class file_priorite:
    def __init__(self,n):
        self.T=[-1 for x in range(n)]
        self.taille=n

    def ajout(self,x):
        for i in self.taille:
            if self.T[i]==-1:
                self.T[i]=x
            else:
                i=self.taille
                while(i>0 and x>=self.T[(i-1)/2]):
                    self.T[i]=self.T[(i-1)/2]
                    i=(i-1)

            self.T[i]=x
            
