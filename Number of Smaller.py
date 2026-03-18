t = 1
while t > 0:
    t -= 1  
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    l = 0
    ans = list()
    for i in b:
        while l < n and a[l] < i:
            l += 1
        ans.append(l)
    print(*ans)
