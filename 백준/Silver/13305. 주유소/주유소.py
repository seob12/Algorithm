import sys

input = sys.stdin.readline

n = int(input())

road = list(map(int,input().split()))
oil = list(map(int,input().split()))

min_price = oil[0]
ans = 0

for i in range(n-1):
    if min_price > oil[i]:
        min_price = oil[i]

    ans += (min_price * road[i])

print(ans)