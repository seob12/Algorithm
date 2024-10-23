n = int(input())
vote = input()

a_cnt = 0
b_cnt = 0

for i in vote:
    if i == 'A':
        a_cnt += 1

    else:
        b_cnt += 1

if a_cnt > b_cnt:
    print('A')
elif b_cnt > a_cnt:
    print('B')
else:
    print('Tie')