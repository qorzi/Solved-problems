import sys
sys.stdin = open('sample_input.txt', 'r')

def f(idx, visited):
    global ans
    visited_tmp = visited[:]

    if idx == N:
        ans += 1
        return

    for i in range(N):
        if visited_tmp[idx][i] == 0:
            visit(idx, i, visited_tmp, 1)
            print(visited)
            f(idx+1, visited_tmp)

            visit(idx, i , visited_tmp, -1)
            print(visited)
def visit(idx, i, visited_tmp, num):
    for j in range(idx, N):
        visited_tmp[j][i] += num
        if i + (j - idx) < N:
            visited_tmp[j][i + (j - idx)] += num
        if i - (j - idx) >= 0:
            visited_tmp[j][i - (j - idx)] += num

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[0]*N for _ in range(N)]
    visited_tmp = []
    ans = 0

    f(0, visited)

    print(f'#{tc} {ans}')
