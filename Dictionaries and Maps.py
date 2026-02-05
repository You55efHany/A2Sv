n = int(input())

c = {}
for i in range(n):
    name, number = input().split()
    c[name] = number
    
while True:
    try:
        name = input()
        if name in c:
            print(f"{name}={c[name]}")
        else:
            print("Not found")
    except EOFError:
        break
