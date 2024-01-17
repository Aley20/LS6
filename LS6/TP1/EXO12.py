print("************ test 1 **************") 
for x in range(0, 10): # Affiche index de 0 à 9 de pas 1
   print(x)

print("************* test 2 **************")   
for x in range(0, 10, 3): # Affiche index de 0 à 9 de pas 3 (0, 3, 6, 9)
   print(x)

print("************* test 3 **************")  #Affiche index de 9 à 0
for x in range(9, -1, -1):                     # NB:Si au lieu de -1 (au milieu), on met 0 
   print(x)                                   # alors affichera index de 9 à 1

print("************* test 4 **************")
for i in range(5):
    print(i)

print("************* test 5 **************")
print(list(range(5, 10))) # res -> [5, 6, 7, 8, 9]

print(list(range(0, 10, 3))) # res -> [0, 3, 6, 9]

print(list(range(-10, -100, -30))) # res-> [-10, -40, -70]

print("************* test 6 **************")
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print("************* test 7 **************")
print(sum(range(4))) # res -> 0+1+2+3=6

print("************* test 8 **************")
for n in range(2, 10):
    for x in range(2, n):
       # print (n,x) # on commencera à (3 2) , (4 2) ... 
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break # on arrête avec la boucle de n on passe au n+1
        else:
         print(n, 'is a prime number')

print("************* test 9 **************")
for num in range(2, 10):        # res -> ..even.. 2 , ..odd..3 , ..even.. 4 ,..odd.. 5 etc.
    if num % 2 == 0: 
        print("Found an even number", num) # Dans les deux cas va faire les test jusqua index 9
        continue
    print("Found an odd number", num) # idem