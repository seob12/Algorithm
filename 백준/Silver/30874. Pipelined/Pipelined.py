n = int(input())

si = list(map(int,input().split()))

ans = 0

arr = []

si.sort()

print(si[n-1] + n-1)