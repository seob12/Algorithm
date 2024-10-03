n = int(input())
arr = list(map(int, input().split()))
b,c = map(int, input().split())

total_test = 0  # 총 감독관 수
semi_test = 0  # 부 감독관 수

for i in range(n):
    if arr[i] > b:   #감독할 수 있는 인원보다 응시자가 크다면
        total_test += 1
        arr[i] -= b
        
    elif arr[i] == b:
        total_test += 1
        arr[i] -= b

    else:
         total_test += 1
         arr[i] = 0
        


for j in range(n):
    while (arr[j] != 0):
        if arr[j] < c or arr[j] == c:
                semi_test += 1
                arr[j] = 0
        else:
            semi_test += (arr[j] // c)
            arr[j] = arr[j] % c


#print(arr)
print(total_test + semi_test)
        
        
        
            
    


    