p,m = map(int, input().split())
arr = []

game = []
waiting = []

for _ in range(p):
    level, name = input().split()
    level = int(level)

    if len(arr) == 0:
        arr.append([(level,name)])
        
    else:
        for x in arr:
            if (x[0][0] - 10 <= level <= x[0][0] + 10) and len(x) < m:
                x.append((level,name))
                break
        else:
            arr.append([(level,name)])
            
for x in arr:
    x.sort(key = lambda x: x[1])
    if len(x) == m:
        print('Started!')
        for r,c in x:
            print(r,c)
            
    else:
        print('Waiting!')
        for r,c in x:
            print(r,c)










