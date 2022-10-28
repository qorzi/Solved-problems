import sys
sys.stdin = open('sample_input.txt', 'r')

def broken(N, new_matrix):

    def shoot(i, j, cnt):

        def explosion(i, j, range_value):
            nonlocal cnt

            if range_value <= 1:
                return
            print(cnt, i, j, range_value)
            cnt += 1
            for di, dj in [[1,0], [-1,0], [0,1], [0,-1]]:
                for r in range(1, range_value):
                    if 0<=i+di*r<H and 0<=j+dj*r<W:
                        explosion_range = new_matrix[i+di*r][j+dj*r]
                        new_matrix[i+di*r][j+dj*r] = 0
                        explosion(i+di*r, j+dj*r, explosion_range)
                        new_matrix[i+di*r][j+dj*r] = explosion_range

        while not matrix[i][j]:
            i += 1
        cnt += 1
        explosion_range = new_matrix[i][j]
        new_matrix[i][j] = 0
        explosion(i, j, explosion_range)
        new_matrix[i][j] = explosion_range

        return cnt

    total_cnt = 0
    for _ in range(N):
        max_cnt = 0
        for j in range(W):
            tmp_cnt = shoot(0, j, 0)
            if tmp_cnt > max_cnt:
                max_cnt = tmp_cnt
        total_cnt += max_cnt
    return total_cnt

T = int(input())
for tc in range(1, 1+1):
    N, W, H = map(int, input().split()) # i = H, j = W
    matrix = [list(map(int, input().split())) for _ in range(H)]

    ans = broken(N, matrix[:])
    print('#{} {}'.format(tc, ans))