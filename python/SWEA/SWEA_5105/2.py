import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    queue = deque()
    #이동 횟수
    cnt_queue = deque()
    cnt_queue.append(0)

    #도착 판별
    arrival_flag = 0

    # 출발지 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]
                queue.append(start)

    # queue를 이용한 경로 탐색은 동시 진행됨.
    while queue and arrival_flag == 0:
        #현재의 i, j
        current = queue.popleft()
        current_i, current_j = current
        #방문기록 남기기
        visited[current_i][current_j] = 1
        #현재의 cnt
        current_cnt = cnt_queue.popleft()

        # 좌, 우, 상, 하 순으로 경로탐색
        for i, j in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            # 사방 탐색 후, 가능한 경로라면, queue에 삽입
            if 0 <= current_i+i < N and 0 <= current_j+j < N:
                if maze[current_i+i][current_j+j] == 0 and visited[current_i+i][current_j+j] == 0:
                    new_root = [current_i+i, current_j+j]
                    queue.append(new_root)
                    cnt_queue.append(current_cnt+1)

                elif maze[current_i + i][current_j + j] == 3:
                    # print('도착')
                    arrival_flag = 1
                    ans = current_cnt
                    break

    if arrival_flag == 0:
        ans = 0

    print(f'#{tc} {ans}')