# 1
def listfichNomC(p,nom):            # p=Path()/'toto/titi/tutu'
    for z in p.glob('**/'+nom):     # p.mkdir(parents=true) 
        print(z)                    # va creer dossier 'toto/titi/tutu'

# Pour tester :
# EXO1.listfichNomC(Path().cwd(),'bip')
# EXO1.listfichNomC(Path().cwd(),'bop')
# EXO1.listfichNomC(Path().cwd(),'bup')

# 2
def listfichNomS(p,nom):
    for z in p.glob('**/*'):
        if z.stem==nom:
            print(z)

# 3
def listfich(p,s):
    for z in p.glob(s+'*'):    # ou for z in p.iterdir():
        if z.is_file():        #        if z.is_file() and z.stem.startswith(s) :
            print(z) 