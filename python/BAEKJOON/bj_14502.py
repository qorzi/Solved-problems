import copy

# N은 세로, M은 가로 수
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 0은 빈칸, 1은 벽, 2는 바이러스

# 풀이 과정
# 1. 탐색으로 가상의 벽을 세운다.
# 2. 바이러스를 사방탐색으로 퍼트린다.
# 3. 안전 영역이 최대가 되는 경우를 저장한다.

max_safe_cnt = 0
visited = copy.deepcopy(matrix)


# 가벽 세우기
def make_wall(depth, matrix, visited):
    global max_safe_cnt
    if depth >= 3:

        tmp_visited = copy.deepcopy(visited)
        # 바이러스 전파
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 2:
                    stack = [(i, j)]
                    while stack:
                        current_i, current_j = stack.pop()
                        if tmp_visited[current_i][current_j] == 0:
                            tmp_visited[current_i][current_j] = 2

                        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:

                            if 0 <= current_i + di < N and 0 <= current_j + dj < M:
                                if matrix[current_i + di][current_j + dj] == 0 and tmp_visited[current_i + di][current_j + dj] == 0:
                                    stack.append((current_i+di, current_j+dj))

        # 안전영역 카운팅
        safe_cnt = 0
        for vi in tmp_visited:
            for vj in vi:
                if vj == 0:
                    safe_cnt += 1

        # print('after-----------------')
        # for x in tmp_visited:
        #     print(x)
        # print('-----------------')

        if max_safe_cnt < safe_cnt:
            max_safe_cnt = safe_cnt

        return

    for i, value_i in enumerate(matrix):
        for j, value_j in enumerate(value_i):
            if value_j == 0:
                matrix[i][j] = 1
                visited[i][j] = 1
                make_wall(depth + 1, matrix, visited)
                matrix[i][j] = 0
                visited[i][j] = 0


make_wall(0, matrix, visited)

print(max_safe_cnt)
