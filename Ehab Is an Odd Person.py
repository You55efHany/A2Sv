n = int(input())
a = list(map(int,input().split()))

od,ev = False,False
for i in a:
    if i % 2 == 1:
        od = True
    else:
        ev = True

if od and ev:
    print(*sorted(a))
else:
    print(*a)
