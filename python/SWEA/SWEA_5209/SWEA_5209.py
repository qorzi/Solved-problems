import sys
sys.stdin = open('sample_input.txt', 'r')

def f(idx, pre_sum):
    global min_sum

    if idx == N:
        if pre_sum < min_sum:
            min_sum = pre_sum
            return

    if min_sum < pre_sum:
        return

    for i in range(N):
        if i not in checked_row:
            checked_row.append(i)
            f(idx + 1, pre_sum + matrix[idx][i])
            checked_row.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    checked_row = []
    min_sum = 99*N

    f(0, 0)

    print(f'#{tc} {min_sum}')