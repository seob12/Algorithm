a,b,c = map(int, input().split())
arr=[]
arr.append(a)
arr.append(b)
arr.append(c)


if a==b and b==c and a==c:
    ans = 10000 + (a*1000)
elif (a==b and b != c):
    ans = 1000 + (a*100)
elif a==c and b!=c:
    ans = 1000+(a*100)
elif b==c and a!=b:
    ans = 1000 + (b*100)
else:
    ans = max(arr) * 100

print(ans)