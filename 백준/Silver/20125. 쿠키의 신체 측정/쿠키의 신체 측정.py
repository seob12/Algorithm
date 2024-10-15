from collections import deque

n = int(input())
arr = [list(map(str,input())) for _ in range(n)]
heart = []
leg = []


left_arm = 0
right_arm = 0
left_leg = 0
right_leg = 0
body = 0

for i in range(n):
    if len(heart) == 1:
        break
    for j in range(n):
        if arr[i][j] == '*':
            heart.append((i+1,j))  # 심장 위치
            print(i+2, j+1)
            break
        

x,y = heart.pop()

left_arm = arr[x][:y].count('*')
right_arm = arr[x][y+1:n].count('*')


for i in range(x+1,n):
    if arr[i][y] == '*':
        body += 1
    else:
        leg.append((i,y))
        break

x,y = leg.pop()

for i in range(x,n):
    if arr[i][y-1] == '*':
        left_leg += 1
    if arr[i][y+1] == '*':
        right_leg += 1

print(left_arm, right_arm, body, left_leg, right_leg)







