from pathlib import Path
def Sauvegarde(L):
    p=Path.cwd()
    p.mkdir(exist_ok=True)
    for (i,s) in enumerate (L) :
        f=p/ ('fich_'+str(i)+'.txt')
        f.write_text(s)
