from itertools import combinations
from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    mbti_lst = list(map(str, input().split()))

    mbti_dict = Counter(mbti_lst)

    max_cnt = max(mbti_dict.values())

    if max_cnt >= 3:
        print(0)

    else:  # max_cnt = 1, 2

        combs = combinations(mbti_lst, 3)

        min_d = 12
        for comb in combs:
            a, b, c = comb

            d = 0
            for i in range(4):
                if a[i] == b[i] == c[i]:
                    pass
                else:
                    d += 2

            if d < min_d:
                min_d = d

        print(min_d)
