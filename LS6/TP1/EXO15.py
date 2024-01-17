def syracuse(p) :
    print(p)
    while(p!=1) : 
      if p%2==0 :
        p=p//2
      else :
        p=3*p+1
      print(p)

p = int(input("Entrez un entier p: "))
syracuse(p)

