base = ['b','1','3','4']

def fetch_nth(n, lst):
    if n < 4:
        lst.append(base[n])
        return
    p,q = divmod(n,3)
    if(q == 0):
        lst.append(base[3])
        fetch_nth(p-1, lst)
    else:
        lst.append(base[q])
        fetch_nth(p, lst)
for i in [4, 10]:
    tmp = []
    fetch_nth(i, tmp)
    print(''.join(reversed(tmp))) 