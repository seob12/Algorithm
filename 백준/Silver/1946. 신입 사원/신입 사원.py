t = int(input())

for _ in range(t):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    arr.sort()
    ans = 1

    max_ = arr[0][1]

    for i in range(1,n):
        if max_ > arr[i][1]:
            ans += 1
            max_ = arr[i][1]

    print(ans)


