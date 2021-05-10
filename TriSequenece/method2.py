base = ['b','1','3','4']

def fetch_xth(x):
    if x < 4:
        return base[x]
    p,q = divmod(x,3)
    if(q == 0):
        return fetch_xth(p-1) + base[3]
    return fetch_xth(p) + base[q]

print('4th term is ',fetch_xth(4)) # 11
print('10th term is ',fetch_xth(10)) # 41