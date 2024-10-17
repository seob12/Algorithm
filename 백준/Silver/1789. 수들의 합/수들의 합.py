s = int(input())
arr = []
ans = 0
cnt = 0

while 1:
    if cnt > s:
        break

    ans += 1

    cnt += ans

print(ans-1)
