def recent_files(p,k):
    LF=sorted ([(f,f.stat().st_mtime) for f in p.glob('*') if f.is_file()],key =lambda x:x[1],reverse=True)

    return [x[0].name for x in LF[:k]]

# pour tester EXO4.recent_files(Path().cwd(),3)