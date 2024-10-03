n = int(input())

# 2차원 평면을 101x101로 초기화
arr = []
grid = [[0] * 101 for _ in range(101)]

# 방향: 0:오른쪽, 1:위, 2:왼쪽, 3:아래
di = [0, -1, 0, 1]  # 상하 이동
dj = [1, 0, -1, 0]  # 좌우 이동

for _ in range(n): 
    x, y, d, g = map(int, input().split())
    arr = [(x, y)]  # 시작점
    x += dj[d]
    y += di[d]
    arr.append((x, y))  # 0세대 끝점
    
    # 드래곤 커브 세대 추가
    for i in range(g):
        cx, cy = arr[-1]  # 마지막 점 기준
        temp = []
        for j in range(len(arr) - 2, -1, -1):  # 역순으로 회전
            px, py = arr[j]
            nx = cx + (cy - py)
            ny = cy - (cx - px)
            temp.append((nx, ny))
        arr.extend(temp)
    
    # 드래곤 커브 그리기
    for px, py in arr:
        grid[px][py] = 1

# 1x1 정사각형 개수 세기
result = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i][j + 1] and grid[i + 1][j] and grid[i + 1][j + 1]:
            result += 1

print(result)
