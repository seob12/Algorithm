s = list(input())

zero = s.count('0')
one = s.count('1')

zero_cnt = zero // 2
one_cnt = one // 2

s.sort()

while zero_cnt != 0:
    s.remove('0')

    zero_cnt -= 1

while one_cnt != 0:
    s.remove('1')

    one_cnt -= 1

print(''.join(s))