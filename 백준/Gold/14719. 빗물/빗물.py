n,m = map(int,input().split())
h = list(map(int,input().split()))
map = [[0 for _ in range(m)]for _ in range(n)]

ans = 0
for i in range(1,m-1):
    left = max(h[:i])
    right = max(h[i+1:])
    mi = min(left,right)
    
    if mi > h[i]:
        ans += (mi-h[i])
        
print(ans)