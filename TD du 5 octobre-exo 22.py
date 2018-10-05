f = open('p022_names.txt', 'r')
l = f.read()
L = l.split(',')
L.sort()
print(L[0])

def compte(chaine):
    somme=0
    for i in chaine:
        somme+=ord(i)
    return somme-68

def total_score():
    somme=0
    for i in L:
        somme+=(i+1)*compte(L[i])
    return somme

print (total_score())