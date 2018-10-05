#exo 55

def test_palindrome(n):
    l=[int(i) for i in str(n)]
    for j in range(len(l)):
        if l[j]!=l[-j-1]:
            return False
    return True


def retournement(n):
    l=str(n)
    L=str()
    for i in range(len(l)):
        L=L+l[-i-1]
    return int(L)
    

def test_peut_donner_palindrome(n):
    #on limite le nombre d'itération à 50
    for i in range(51):
        if test_palindrome(n+retournement(n))==True:
            return True
        else:
            n+=retournement(n)
    return False


def compte_lychrel():
    somme=0
    for i in range(10001):
        if test_peut_donner_palindrome(i)==False:
            somme+=1
    return somme


assert test_palindrome(12321)==True
assert retournement(12345)==54321
assert test_peut_donner_palindrome(349)==True
assert test_peut_donner_palindrome(196)==False

print(compte_lychrel())