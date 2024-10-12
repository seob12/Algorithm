n = input()
arr = []

for i in n:
    arr.append(i.lower())
    
arr_2 = []
arr_3 = {}

for j in list(set(arr)):
    arr_2.append(arr.count(j))
    arr_3[j] = arr.count(j)
    
arr_3 = sorted(arr_3.items(),key=lambda x:x[1], reverse = True)
    
if arr_2.count(max(arr_2)) > 1:
    print('?')
else:
    print(arr_3[0][0].upper())



    