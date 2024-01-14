# isSquare returns True if the string argument is a square and False otherwise
# This runs in O(n)
def isSquare(w):
    a= int(len(w)/2) 
    return w[:a] == w[a:]


# squarefreereturns True if the string argument coesn't contain a square inside and false otherwise

def squarefree(w):
    for i in range(len(w)):
        for j in range(i+1,len(w)+1):
            if( isSquare(w[i:j])):
                print("Square Found", w, w[i:j])
                return False
    return True

# Return all the squarefree words in a list of words
def findSquareFree(w):
    retList = []
    for i in w:
        if(squarefree(i)):
            retList.append(i)
    return retList


# Return the list of all pairs of words concatenated
def product(a,b):
    retList= []
    for i in a:
        for j in b:
            retList.append(i+j)
    return retList

twoLetter = ["ab","ac","cb"]
# The letter a appears only in 0 mod 3 positions
threeLetter = ["abc", "acb", "bcb", "cbc"]

# The letter a appears only in 0 mod 3 and 1 mod 3 positions
t1 = ["abc", "acb", "bcb", "cbc", "cab", "bac"] 
def induct(n,s):
    retValue = []
    if(n == 2):
        return s
    else:
        temp1 = induct(n-1,s)
        temp2 = product(temp1, temp1)
        return findSquareFree(temp2)
