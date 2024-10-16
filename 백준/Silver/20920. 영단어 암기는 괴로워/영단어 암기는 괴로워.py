n,m = map(int,input().split())
arr = []
dic = dict()
di = dict()
arr_1 = []

for _ in range(n):
    word = input()
    if len(word) < m:
        continue
    else:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

dic = dict(sorted(dic.items(), key = lambda x: (-x[1],-len(x[0]),x[0])))

for x,y in dic.items():
    print(x)

