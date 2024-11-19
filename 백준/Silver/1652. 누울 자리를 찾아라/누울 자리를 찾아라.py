n = int(input())

arr = [list(map(str,input())) for _ in range(n)]

garo = 0
sero = 0

for i in range(n):
    tmp, tp = 0,0
    for j in range(n):
        if arr[i][j] == '.':
            tmp += 1
        else:
            tmp = 0

        if tmp == 2:
            garo += 1

        if arr[j][i] == '.':
            tp += 1
        else:
            tp = 0
            
        if tp == 2:
            sero += 1
            
print(garo, sero)