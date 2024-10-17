p = int(input())


for _ in range(p):
    n = int(input())
    arr = list(map(int,input().split()))
    dp = [0*n]
    stock = []
    ans = 0

    max_price = 0
    for i in range(n-1,-1,-1):
        if arr[i] > max_price:
            max_price = arr[i]
        else:
            ans += (max_price - arr[i])

    print(ans)
