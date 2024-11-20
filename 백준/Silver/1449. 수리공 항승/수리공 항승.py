n,l = map(int,input().split())
arr = [0] * 10000

water = list(map(int, input().split()))
water.sort()
ans = 0
for i in water:
    if arr[i] == 0:
        ans += 1
        for j in range(i,i+l):
            arr[j] = 1

print(ans)
