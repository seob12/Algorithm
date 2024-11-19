import itertools

arr = []

for _ in range(9):
    arr.append(int(input()))

arr.sort()

for i in itertools.combinations(arr,7):
    if sum(i) == 100:
        i = list(i)
        i.sort()

        for j in i:
            print(j)
            
        break




