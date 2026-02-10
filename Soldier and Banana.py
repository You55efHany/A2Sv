k, n, w = map(int, input().split())

ans = max(w * (w + 1) / 2 * k - n, 0)
print(int(ans))
