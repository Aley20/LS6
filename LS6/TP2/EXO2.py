def test(): 
       L=[1,2,3,4]
       L1=L # Même list quand on modifie L1 on modifie aussi L , inversement
       #print(L1)
       L2=L[:] # on fait une copie , si on modifie L2 , on modifie pas L1
       #print(L2)
       L1[1]=18
       #L2[1]=20
       print(L)
       print(L1)
       print(L2)

#import EXO2
#import importlib
#EXO2.test()
#Pour modif 
#importlib.reload(nomfich)
#import importlib

test()