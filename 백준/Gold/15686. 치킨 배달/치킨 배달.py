import itertools

n,m = map(int, input().split())
array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

house = []
chicken = []
distance = []

for i in range(n):
    for j in range(n):
        if array[i][j] == 0:
            continue
        if array[i][j] == 1:
            house.append((i,j))
        if array[i][j] == 2:
            chicken.append((i,j))

candidates = list(itertools.combinations(chicken,m))

#print(candidate)

def get_sum(candidate):
    result = 0

    for r1,c1 in house:
        temp = 1e9
        for r2,c2 in candidate:
            temp = min(temp,abs(r1-r2) + abs(c1-c2))
        result += temp
    
    return result
        
#print(min(distance))
result = 1e9

for k in candidates:
    result = min(result,get_sum(k))

print(result)

        

            