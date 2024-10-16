from collections import deque

n = int(input())
q = deque()

for i in range(1,n+1):
    q.append(i)

while 1:
    if len(q) == 1:  # 한장 남으면 종료
        break

    q.popleft()  # 제일 위의 카드 버리기

    num = q.popleft()
    q.append(num)


m = q.popleft()
print(m)