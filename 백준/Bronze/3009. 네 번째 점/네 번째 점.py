arr_x = []
arr_y = []
for _ in range(3):
    a,b = map(int,input().split())
    arr_x.append(a)
    arr_y.append(b)

for i in list(set(arr_x)):
    if arr_x.count(i) == 1:
        ans_x = i

for j in list(set(arr_y)):
    if arr_y.count(j) == 1:
        ans_y = j


print(ans_x, ans_y)