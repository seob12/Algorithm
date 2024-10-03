# 마법사상어와 파이어볼

n,M,k = map(int, input().split())
vec = []
arr = [[[] for _ in range(n)] for _ in range(n)]


di = [-1,-1,0,1,1,1,0,-1]
dj = [0,1,1,1,0,-1,-1,-1]

for _ in range(M):
    r,c,m,s,d = map(int, input().split())
    vec.append((r-1,c-1,m,s,d))
    

for _ in range(k):
    while vec:
        cr,cc,cm,cs,cd = vec.pop(0)
        nr = (cr + di[cd] * cs)%n
        nc = (cc + dj[cd] * cs)%n
        arr[nr][nc].append((cm,cs,cd))
        
    for i in range(n):
        for j in range(n):
            if len(arr[i][j]) >= 2:
                sum_m, sum_s, cnt, zzak, hol = 0,0,len(arr[i][j]),0,0
                while arr[i][j]:
                    cm,cs,cd = arr[i][j].pop(0)
                    sum_m += cm
                    sum_s += cs
                    if cd % 2 == 0:
                        zzak += 1
                    else:
                        hol += 1
                if zzak == cnt or hol == cnt:
                    nd = [0,2,4,6]
                else:
                    nd = [1,3,5,7]
                    
                if sum_m // 5:
                    for d in nd:
                        vec.append((i,j,sum_m//5, sum_s//cnt, d))
                        
            if len(arr[i][j]) == 1:
                cm,cs,cd = arr[i][j].pop()
                vec.append((i,j,cm,cs,cd))
                
print(sum([f[2] for f in vec]))
                