f = open('p022_names.txt', 'r')
l = f.read()
L = l.split(',')
L.sort()
print(L)

def compte(chaine):
    somme=0
    for i in chaine:
        somme+=ord(i)-64
    return somme+60

Score=[compte(L[i]) for i in range(len(L))]

print(Score)

def total_score():
    somme=0
    for i in range(len(L)):
        somme+=(i+1)*Score[i]
    return somme
    
    
print (total_score())