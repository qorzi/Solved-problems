import sys
sys.stdin = open('sample_input.txt', 'r')
from collections import deque

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    matrix = [[0]*(V+1) for _ in range(V+1)]
    for start, end in lst:
        matrix[start][end] = 1
        matrix[end][start] = 1

    queue = deque()
    queue.append(S)
    visited = []
    cnt_que = deque()
    cnt_que.append(0)
    # 도착 유무 판별
    flag = 0
    while queue:
        current = queue.popleft()
        current_cnt = cnt_que.popleft()
        if current not in visited:
            visited.append(current)
        if current != G:
            for destination in range(V+1):
                if matrix[current][destination] and destination not in visited:
                    queue.append(destination)
                    cnt_que.append(current_cnt+1)
        elif current == G:
            flag = 1
            # print('도착', current_cnt)
            break
    if flag == 0:
        current_cnt = 0
    print(f'#{tc} {current_cnt}')