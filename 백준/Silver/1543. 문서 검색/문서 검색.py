s = input()
find = input()
ans = 0
idx = len(find)
i = 0

while i < len(s):
    lst = s[i:i+idx]
    k = ''.join(lst)

    if find == k:
        ans += 1
        i += idx
    else:
        i += 1


print(ans)