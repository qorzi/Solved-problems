import sys
sys.stdin = open('input_1210.txt', 'r')

T = 10
for tc in range(1, 11):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    visited = list()

    for j in range(100):
        if data[99][j] == 2:
            now_i = 99
            now_j = j

    while now_i > 0:
        # print(now_i, now_j) if tc == 1 else 0
        visited += [[now_i, now_j]]
        if (now_j-1 >= 0) and (data[now_i][now_j-1] == 1) and ([now_i, now_j-1] not in visited):
            now_j -= 1

        elif (now_j+1 < 100) and (data[now_i][now_j+1] == 1) and ([now_i, now_j+1] not in visited):
            now_j += 1

        else:
            now_i -= 1
        # print(visited)
    print(f'#{tc} {now_j}')