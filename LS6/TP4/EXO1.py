import random

def Deviner(k):
    n=random.randint(0,k)
    trouve=False

    try :
        while not trouve:
            try :
                v=input ("veuillez deviner le nombre : ")
                val=int(v)
                if val>n :
                    print("Nombre trop grand")
                elif val<n :
                    print("Nombre trop petit")
                else :
                    print("Bravo !")
                    trouve=True
            except ValueError :
                print ("proposez uniquement des nombres entiers")
    except KeyboardInterrupt :
        print('\n le nombre était ',str(n))
    finally :
        print("Au revoir")

Deviner(5)