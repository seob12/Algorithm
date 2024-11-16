from collections import deque

t = int(input())

def bfs():
    while q:
        x,y = q.popleft()

        if abs(beer_x - x) + abs(beer_y - y) <= 1000:
            print('happy')
            return
        else:
            for i in range(n):
                if not v[i]:
                    r,c = store[i]

                    if abs(r-x) + abs(c-y) <= 1000:
                        q.append((r,c))
                        v[i] = 1


    print('sad')
    return









for _ in range(t):
    n = int(input())

    home_x, home_y = map(int, input().split())
    store = []
    q = deque()

    for _ in range(n):
        x,y = map(int,input().split())
        store.append((x,y))

    beer_x, beer_y = map(int,input().split())

    q.append((home_x,home_y))
    beer = 20
    v = [0 for _ in range(n+1)]

    bfs()