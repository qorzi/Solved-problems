import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

for _ in range(10):
    tc = int(input())
    password = deque(map(int, input().split()))

    minus_cnt = 0
    while password[-1] != 0:

        if minus_cnt == 5:
            minus_cnt = 0
        minus_cnt += 1

        # print(password, minus_cnt)

        if password[0] != 0 and (password[0] - minus_cnt) > 0:
            tmp = password.popleft() - minus_cnt
            password.append(tmp)
        elif password[0] == 0 or (password[0] - minus_cnt) <= 0:
            password.popleft()
            password.append(0)

    password = list(password)

    print(f'#{tc}', end=' ')
    print(*password)
