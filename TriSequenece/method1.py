def nextVal(x):
    nextTerm = x
    lastDigit = x%10
    x = x//10
    if(lastDigit == 0):
        return 1
    if(lastDigit == 1):
        nextTerm = x*10 + 3
    elif(lastDigit == 3):
        nextTerm = x*10 + 4
    else:
        nextTerm = nextVal(x)*10 + 1
    return nextTerm
    

def getSeqTerm(n):
    nextTerm = 1
    while(n>1):
        n = n - 1
        nextTerm = nextVal(nextTerm)
    return nextTerm

print('4th term is ',getSeqTerm(4)) # 11
print('10th term is ',getSeqTerm(10)) # 41

