#n, k = map(int, input().split())
#a = list(map(int, input().split()))

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    flag = False
    for i in range(1,n):
        if a[i] != a[i-1] and a[i] != a[i-1]+1:
            flag = True
            break
    if(flag):
        print("NO")
    else:
        print("YES")
