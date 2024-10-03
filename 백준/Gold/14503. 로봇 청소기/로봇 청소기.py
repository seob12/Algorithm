n,m = map(int, input().split())
ci,cj,d = map(int, input().split())
array = []

for _ in range(n):
    array.append(list(map(int, input().split())))


di = [-1,0,1,0]   # 북동남서
dj = [0,1,0,-1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(ci,cj,d):
    result = 0
    while 1:
        if array[ci][cj] == 0:   # 현재 칸이 빈칸이라면 청소하고 카운트 증가
            array[ci][cj] = -1
            result += 1

        for i in range(4):   # 주변 4방향 보면서 청소안한칸 있는 지 확인
            d = (d-1)%4
            ni, nj = ci+di[d], cj+dj[d]
            if in_range(ni, nj) and array[ni][nj] == 0:
                ci, cj = ni, nj
                break

        else:   # 현재 칸이 벽이라면
            ci, cj = ci + di[d] * (-1), cj + dj[d] * (-1)
            if in_range(ci, cj) and array[ci][cj] == 1 or not in_range(ci, cj):
                print(result)
                return
            


bfs(ci,cj,d)

    
            