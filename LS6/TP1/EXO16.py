##################### Question 1 #####################
def count_banks(s) :
   return s.count(" ") # méthode de la classe str qui compte le nombre d'occurrences 
                       # d'un caractère spécifique dans une chaîne de caractères

s="hello hey oo"
print(str(count_banks(s)))    

#ss = input("Entrez une chaîne de caractères: ")
#print("Le nombre d'espaces dans la chaîne est:", count_banks(ss))

##################### Question 2 #####################
def is_palindrome(s) :
    return s == s[::-1]

print(is_palindrome("racecar")) # True
print(is_palindrome("232")) # True
print(is_palindrome("abc")) # False

#var = input(("Entrez une chaîne de caractère : "))
#print(is_palindrome(var))

##################### Question 3 #####################
def count(s,o) :
    return s.count(o)

print(count("aljjsdfajajjjj", "jj")) # res -> 3
print(count("jjj", "jj")) # res -> 1

