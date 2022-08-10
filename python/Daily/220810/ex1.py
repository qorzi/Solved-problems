import sys
sys.stdin = open('ex1_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    di = [0, 0, -1, 1] # 상 하 좌 우
    dj = [-1, 1, 0, 0]

    all_list = []
    for i in range(0, N):
        for j in range(0, N):
            tmp_value = 0
            for k in range(4): #이웃한 칸 개수(상하좌우, 4개)
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N: #유효한 인덱스면
                    pass
                    # print(abs(arr[ni][nj]-arr[i][j]))
                    tmp_value += abs(arr[ni][nj]-arr[i][j])
            all_list += [tmp_value]
    print(f'#{tc} {sum(all_list)}')