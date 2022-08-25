import sys
sys.stdin = open('sample_input.txt', 'r')
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = []
    queue = deque()
    cnt = 0

    #도착 판별
    arrival_flag = 0

    # 출발지 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]
                tmp = (start, cnt)
                queue.append(tmp)

    # queue를 이용한 경로 탐색은 동시 진행됨.
    while queue:
        tmp = queue.popleft()
        tmp = list(tmp)
        #현재의 [current_i, current_j]
        current = tmp[0]
        #방문기록 남기기
        visited.append(current)
        #현재 i, j
        current_i, current_j = current
        #현재의 cnt
        current_cnt = tmp[1]

        # 좌, 우, 상, 하 순으로 경로탐색
        for i, j in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            # 사방 탐색 후, 가능한 경로라면, queue에 삽입
            if 0 <= current_i+i < N and 0 <= current_j+j < N:
                if maze[current_i+i][current_j+j] == 0 and [current_i+i, current_j+j] not in visited:
                    new_root = [current_i+i, current_j+j]
                    tmp = [new_root, current_cnt+1]
                    queue.append(tmp)

                if maze[current_i + i][current_j + j] == 3:
                    # print('도착')
                    arrival_flag = 1
        print(queue)


    if arrival_flag == 0:
        cnt = 0
    else:
        cnt = current_cnt

    print(f'#{tc} {cnt}')