from copy import deepcopy
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

def gravity(matrix):
    rotate_matrix = list(map(list, zip(*matrix[::-1])))
    print('rotate')
    check(rotate_matrix)
    print('rotate')
    for i in range(W):
        lst = matrix.pop()
        new_lst = list(filter(lambda x: x == 0, lst))
        num = H - len(new_lst)
        for _ in range(num):
            new_lst.append(0)
        matrix.append(new_lst)
    new_matrix = list(map(list, zip(*rotate_matrix)))[::-1]
    print('gravity')
    check(new_matrix)
    print('gravity')
    return new_matrix
    # check(new_matrix)


def break_block(matrix, i, j, range_value, shoot_cnt):
    start = [(i, j, range_value)]
    print(i, j)
    while start:

        i, j, range_value = start.pop(0)
        if matrix[i][j] == 0:
            continue
        matrix[i][j] = 0

        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            for r in range(1, range_value):
                if 0 <= i + di * r < H and 0 <= j + dj * r < W:
                    start.append((i + di * r, j + dj * r, matrix[i + di * r][j + dj * r]))

    new_matrix = gravity(matrix)
    shoot(new_matrix, shoot_cnt+1)

def shoot(matrix, shoot_cnt):
    if shoot_cnt >= 3:
        global max_cnt
        check(matrix)
        cnt = count_all(matrix)
        print(cnt)
        print()
        if cnt < max_cnt:
            max_cnt = cnt
        return
    # 가로 방향으로 구슬 떨어질곳 서치
    for j in range(W):
        i = 0
        while matrix[i][j] == 0:  # 아래로 낙하
            i += 1
            if i >= H-1:  # 닿을 곳이 없다면 다음
                break
        new_matrix = deepcopy(matrix)
        break_block(new_matrix, i, j, matrix[i][j], shoot_cnt)

T = int(input())
for tc in range(1, 1+1):
    N, W, H = map(int, input().split()) # i = H, j = W
    matrix = [list(map(int, input().split())) for _ in range(H)]

    max_cnt = 999999
    shoot(matrix, 0)

    print('#{} {}'.format(tc, max_cnt))