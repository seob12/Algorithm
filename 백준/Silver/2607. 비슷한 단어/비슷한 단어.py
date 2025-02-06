n = int(input())

arr = [input() for _ in range(n)]

target = list(arr[0])
ans = 0

for i in range(1,n):
    compare = target[:]
    cnt = 0
    word = list(arr[i])

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(compare) < 2:
        ans += 1

print(ans)
