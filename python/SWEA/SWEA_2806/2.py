import sys
sys.stdin = open('sample_input.txt', 'r')

def f(idx):
    global ans

    if idx == N:
        ans += 1
        return
    for i in range(N):
        # print(visited)
        if visited[idx][i] == 0:
            for j in range(idx, N):
                visited[j][i] += 1
                if i + (j - idx) < N:
                    visited[j][i+(j-idx)] += 1
                if i - (j - idx) >= 0:
                    visited[j][i-(j-idx)] += 1
            # print(visited)
            f(idx+1)

            for j in range(idx, N):
                visited[j][i] -= 1
                if i + (j - idx) < N:
                    visited[j][i+(j-idx)] -= 1
                if i - (j - idx) >= 0:
                    visited[j][i-(j-idx)] -= 1
            # print(visited)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[0]*N for _ in range(N)]
    sel = []
    ans = 0

    f(0)

    print(f'#{tc} {ans}')