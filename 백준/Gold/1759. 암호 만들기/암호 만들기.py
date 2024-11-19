import itertools

n,m = map(int,input().split())

s = list(map(str, input().split()))

s.sort()



for i in itertools.combinations(s,n):
    jaum_cnt = 0
    moum_cnt = 0
    for j in i:
        if j in ['a','e','i','o','u']:
            moum_cnt += 1
        elif j not in ['a','e','i','o','u']:
            jaum_cnt += 1

        if moum_cnt > 0 and jaum_cnt > 1:
            k = ''.join(i)
            print(k)
            break