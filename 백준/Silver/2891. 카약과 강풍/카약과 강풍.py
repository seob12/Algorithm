n,s,r = map(int, input().split())

team = [1 for _ in range(n+2)]

damage = list(map(int, input().split()))
extra = list(map(int,input().split()))

for i in extra:
    i = i - 1
    team[i] += 1

for i in damage:
    i = i - 1
    team[i] -= 1

cnt = 0

for i in range(1,n):
    if team[i] > 1:
        if team[i-1] == 0:
            team[i-1] += 1
            team[i] -= 1
        elif team[i+1] == 0:
            team[i+1] += 1
            team[i] -= 1

print(team.count(0))




