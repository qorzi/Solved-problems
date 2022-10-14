import sys
sys.stdin = open('sample_input.txt', 'r')

def count_line(i, j):



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = matrix[:]

    core = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j]:
                if i == 0 or i == N-1 or j == 0 or j == N-1:
                    core.append([i,j,0])
                else:
                    core.append([i,j,1])
    print(core)
    for i, j, on_off in core:
        if on_off:
            count_line(i, j)

    for i in visited:
        print(i)