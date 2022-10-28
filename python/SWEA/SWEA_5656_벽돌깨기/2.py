import sys
sys.stdin = open('sample_input.txt', 'r')

def check(visited):
    for i in visited:
        print(i)

def count_all(matrix):
    cnt = 0
    for i in matrix:
        for j in i:
            if j:
                cnt += 1
    return cnt

def shoot(shoot_cnt, visited):
    new_visited = visited[:]
    if shoot_cnt >= 3:
        global max_broken_cnt
        check(new_visited)
        broken_cnt = count_all(new_visited)
        print(broken_cnt)
        if max_broken_cnt < broken_cnt:
            max_broken_cnt = broken_cnt
        print()
        return

    for j in range(W):
        # 구슬에 터질 곳 서치
        i = 0
        while matrix[i][j] == 0 or (matrix[i][j] and new_visited[i][j]):
            i += 1
            if i >= H:
                return
        print(shoot_cnt, i, j, new_matrix[i][j])
        explosion(i, j, new_matrix[i][j], shoot_cnt+1, new_visited)

def explosion(i, j, range_value, shoot_cnt, visited):
    new_visited = visited[:]
    if range_value > 1:
        start = [(i, j, range_value)]
        while start:
            print(start)
            i, j, range_value = start.pop(0)
            if new_visited[i][j]:
                continue

            new_visited[i][j] = 1

            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                for r in range(1, range_value):
                    if 0 <= i + di * r < H and 0 <= j + dj * r < W:
                        if new_visited[i + di * r][j + dj * r] == 0 and new_matrix[i + di * r][j + dj * r]:
                            start.append((i + di * r, j + dj * r, new_matrix[i + di * r][j + dj * r]))
    else:
        new_visited[i][j] = 1
    shoot(shoot_cnt, new_visited)

T = int(input())
for tc in range(1, 1+1):
    N, W, H = map(int, input().split()) # i = H, j = W
    matrix = [list(map(int, input().split())) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    total_default = count_all(matrix)
    print(total_default)

    max_broken_cnt = 0
    new_matrix = matrix[:]
    shoot(0, visited)
    ans = total_default - max_broken_cnt

    print('#{} {}'.format(tc, ans))