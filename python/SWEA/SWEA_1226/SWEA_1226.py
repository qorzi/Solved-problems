import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    queue = []

    # 도착 판별
    arrival_flag = 0

    # 출발지 찾기
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = [i, j]
                queue.append(start)

    # queue를 이용한 경로 탐색은 동시 진행됨.
    while queue and arrival_flag == 0:
        # 현재의 i, j
        current = queue.pop(0)
        current_i, current_j = current
        # 방문기록 남기기
        visited[current_i][current_j] = 1

        # 좌, 우, 상, 하 순으로 경로탐색
        for i, j in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            # 사방 탐색 후, 가능한 경로라면, queue에 삽입
            if 0 <= current_i + i < 16 and 0 <= current_j + j < 16:
                if maze[current_i + i][current_j + j] == 0 and visited[current_i + i][current_j + j] == 0:
                    new_root = [current_i + i, current_j + j]
                    queue.append(new_root)

                elif maze[current_i + i][current_j + j] == 3:
                    # print('도착')
                    arrival_flag = 1
                    ans = 1
                    break

    if arrival_flag == 0:
        ans = 0

    print(f'#{tc} {ans}')