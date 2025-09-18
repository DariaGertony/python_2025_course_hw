a = list(map(int,input().split()))
a.sort()
p1  =0
p2 = len(a)-1
f = list(range(len(a)))

pf = len(f)-1
while p1 != p2:
    print(f)
    if abs(a[p1]) > abs(a[p2]):
        f[pf] = abs(a[p1])
        pf = pf-1
        p1 = p1+1
    else:
        f[pf] = abs(a[p2])
        pf = pf-1
        p2 = p2-1
f[pf] = a[p2]
print(f)
