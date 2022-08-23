

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    index_col = []
    for i in range(N):
        index_col += i
    checked_col = [0]*N
    min_sum = 99*N
    pre_sum = 0
    col = 0

    while index_col[col] < N:
        if checked_col[col] < col:
            if col % 2 == 0:
                index_col[0], index_col[col] = index_col[col], index_col[0]
            else:
                index_col[checked_col[col]], index_col[col] = index_col[col], index_col[checked_col[col]]
            result.append(arr[:])







    print(f'#{tc} {min_sum}')