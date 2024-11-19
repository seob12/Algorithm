import itertools

n,m = map(int,input().split())

arr = list(map(int, input().split()))

lst = list(itertools.combinations(arr, 3))

ans = []

for i in lst:
    ans.append(sum(i))

ans.sort(reverse = True)

for i in ans:
    if i > m:
        continue
    else:
        print(i)
        break