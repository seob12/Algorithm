from collections import deque

arr = [deque(list(map(int, input()))) for _ in range(4)]

def right(num,d):
    if num > 3:
        return
    
    if arr[num][6] != arr[num-1][2]:
        right(num+1, -d)

        arr[num].rotate(d)




def left(num, d):
    if num < 0:
        return
    
    if arr[num][2] != arr[num+1][6]:
        left(num-1, -d)

        arr[num].rotate(d)



for _ in range(int(input())):
    num, d = map(int, input().split())
    num -= 1

    left(num-1, -d)
    right(num+1, -d)

    arr[num].rotate(d)


result = 0


for i in range(4):
    if arr[i][0] == 1:
        result += (2 ** i)

print(result)
    
