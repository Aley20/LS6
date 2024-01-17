#n = int(input("Saisissez un entier : "))
#if n>0: 
#    print("positif") 
#elif n==0: 
#    print("zero") 
#else:
#    print("negatif")

    # import EXO10
    # import importlib
    # importlib.reload(EXO10)
    
a = int(input(" 0 pour True ou 1 pour False "))
b = int(input(" 0 pour True ou 1 pour False "))

if a>1 or a<0: 
    raise ValueError("U1: vous devez choisir entre 0 pour True ou 1 pour False")
elif a==0: 
    print("True") 
else:
    print("False")

if b>1 or b<0: 
    raise ValueError("U2: vous devez choisir entre 0 pour True ou 1 pour False")
elif b==0: 
    print("True") 
else:
    print("False")

#while not (verif(a) & verif(b)) :
#    print("Veuillez saisir 'True' ou 'False' pour a et b.")
#    a = input("Saisissez 'True' ou 'False' pour a : ").strip()
#    b = input("Saisissez 'True' ou 'False' pour b : ").strip()
#