import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    #Q_LR의 idx에서 [L, R]
    Q_LR = [list(map(int, input().split())) for _ in range(Q)]

    #상자
    box = [0]*N

    for idx, i in enumerate(Q_LR):
        L, R = i
        for j in range(L-1, R):
            box[j] = int(idx+1)

    print(f'#{tc}', end=' ')
    print(*box)
