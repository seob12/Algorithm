t = int(input())

for _ in range(t):
    n,k,ID,m = map(int,input().split())
    scores = {i: [0] * (k+1) for i in range(1,n+1)}
    cnt = [0] * (n+1)
    order = [0] * (n+1)
    for i in range(m):
        id, j, s = map(int,input().split())
        scores[id][j] = max(scores[id][j],s)
        cnt[id] += 1
        order[id] = i



    print(sorted(scores, key=lambda x:[-sum(scores[x]), cnt[x], order[x]]).index(ID)+1)

