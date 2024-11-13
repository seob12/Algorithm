k = int(input())

n = 1
i = 0
arr = []

while n < k:
    n = 2 ** i
    i += 1

tmp = n
cnt = 0

if k != n:
    while k:
        tmp //= 2
        if k >= tmp:
            k = k - tmp
            cnt += 1
        else:
            cnt += 1

print(n, cnt)
