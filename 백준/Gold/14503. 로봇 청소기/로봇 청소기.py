n,m = map(int,input().split())
ci,cj,d = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

visited = [[0]*m for _ in range(n)]

di = [-1,0,1,0]  # 북동남서
dj = [0,1,0,-1]
result = 1
#q = deque()
#q.append((x,y))
flag = 1
visited[ci][cj] = 1

while (1):
    #ci, cj = q.popleft()  # 큐에서 꺼내
    cnt = 0
    # if arr[ci][cj] == 0:
    #     result += 1
    #     #visited[ci][cj] = 1
    #     arr[ci][cj] = -1   # 청소함

    for vec in range(4):    # 4방향 돌면서
        d = (d-1)%4
        nx = ci + di[d]
        ny = cj + dj[d]

# 4방향 중 빈칸이 있는 경우
        if arr[nx][ny] == 0 and in_range(nx,ny):
            if visited[nx][ny] == 0:
                ci = nx
                cj = ny
                cnt += 1  # 청소함
                arr[ci][cj] = -1  # 청소함
                result += 1
                visited[ci][cj] = 1
                break

    if cnt == 0:  # 빈칸이없는경우
        if arr[ci - di[d]][cj-dj[d]] == 1:
            print(result)
            break
        else:
            ci = ci - di[d]
            cj = cj - dj[d]
        
        
