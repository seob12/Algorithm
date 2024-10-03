n,m,x,y,k = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

#dice = [[0,0,0,0,0,0]*m for _ in range(n)]
dice_num = [0,0,0,0,0,0]

move = list(map(int,input().split()))

di = [0,0,-1,1]
dj = [1,-1,0,0]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m


for d in move:
    d -= 1
    
    nx = x + di[d]
    ny = y + dj[d]

    if in_range(nx,ny):  # 동서북남
        if d == 0:
            dice_num = [dice_num[3]] + [dice_num[1]] + [dice_num[0]] + [dice_num[5]] + [dice_num[4]] + [dice_num[2]]
        elif d == 1:
            dice_num = [dice_num[2]] + [dice_num[1]] + [dice_num[5]] + [dice_num[0]] + [dice_num[4]] + [dice_num[3]]
        elif d == 2:
            dice_num = [dice_num[4]] + [dice_num[0]] + [dice_num[2]] + [dice_num[3]] + [dice_num[5]] + [dice_num[1]]
        elif d == 3:
            dice_num = [dice_num[1]] + [dice_num[5]] + [dice_num[2]] + [dice_num[3]] + [dice_num[0]] + [dice_num[4]]

        x = nx
        y = ny

        if arr[nx][ny] == 0:
            arr[nx][ny] = dice_num[5]
        else:
            dice_num[5] = arr[nx][ny]
            arr[nx][ny] = 0

        print(dice_num[0])

    else:
        continue