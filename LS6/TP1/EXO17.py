############ Compare le temps d'éxecution de l''implémentation ######
import time

def count(s,o) :
    start_time = time.time()
    count=s.count(o)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Temps d'éxecution: ",execution_time)
    return count

print(count("Speedy␣Gonzales"* 10000 ,"ee")) # res -> 3
