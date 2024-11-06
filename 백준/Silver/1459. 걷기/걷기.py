x,y,w,s = map(int,input().split())

ans = 0

now_x, now_y = 0,0

cost1 = (x+y)*w

if (x+y) % 2 == 0:
    cost2 = max(x,y) * s
else:
    cost2 = (max(x,y) - 1 ) * s + w

cost3 = (min(x,y)*s) + ((max(x,y) - min(x,y)) * w)

ans = min(min(cost1,cost2), cost3)

print(ans)