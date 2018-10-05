def somme_chiffre(N):
    l=str(N)
    somme=0
    for i in range(len(l)):
        somme+=int(l[i])
    return somme

def solve(N):
    return somme_chiffre(N)

assert solve(123)==6

print (solve(2**1000))