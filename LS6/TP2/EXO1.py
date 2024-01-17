def exo1 (matrice) :
    count=0
    for i in range (1,len(matrice)-1):
        for j in range (1,len(matrice[i])-1):
            if matrice[i][j]>matrice[i-1][j] and matrice[i][j]>matrice[i+1][j] and matrice[i][j]>matrice[i][j-1] and matrice[i][j]>matrice[i][j+1]:
                count+=1
         
    return count


matrix=[[1,4,9,1,4],[4,8,1,2,5],[4,1,3,4,6],[5,0,4,7,6],[2,4,9,1,5]]
print(exo1(matrix))

