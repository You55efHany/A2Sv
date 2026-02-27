n, k = map(int, input().split())
a = a = list(map(int, input().split()))
a.sort()

if k == 0:
    if(a[0] == 1):
        print(-1)
    else:
        print(1)
    exit()

for i in range(len(a)):
    if i != len(a) - 1:
        if a[i] == a[i+1]:
            continue
    if i+1 == k:
        print(a[i])
        exit()
print(-1)

