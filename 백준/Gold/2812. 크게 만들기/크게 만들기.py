import itertools

n,k = map(int,input().split())
num = list(map(int, input()))
ans = []
ans.append(num[0])

for i in range(1,n):
    while len(ans) > 0 and k > 0:
        if num[i] > ans[-1]:
            ans.pop()
            k -= 1
        else:
            break

    ans.append(num[i])



if k > 0:
    print(''.join(map(str, ans[:-k])))
else:
    print(''.join(map(str, ans)))
