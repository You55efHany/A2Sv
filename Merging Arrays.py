n,m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

p1,p2 = 0,0

ans = list()
while p1 < n or p2 < m:
    if p2 >= m:
        ans.append(a[p1])
        p1 += 1
    elif p1 >= n:
        ans.append(b[p2])
        p2 += 1
    elif a[p1] < b[p2]:
        ans.append(a[p1])
        p1 += 1
    else:
        ans.append(b[p2])
        p2 += 1
        
print(*ans)
        
