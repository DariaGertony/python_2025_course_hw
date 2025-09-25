
def S(h1:int, h2:int, l:int, r:int) -> int:
    return abs(min(h1,h2)*(l-r))

a = list(map(int,input().split()))
p1  =0
p2 = len(a)-1
ans:int = 0
while p1 != p2:
    ans = max(ans, S(a[p1],a[p2],p1,p2))
    if(a[p1] < a[p2]):
        p1 = p1+1
    else:
        p2 = p2-1
print(ans)



