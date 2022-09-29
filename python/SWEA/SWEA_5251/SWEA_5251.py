import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    max_num = 1000*N*N
    matrix = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        matrix[s][e] = w

    visited = [0]*(N+1)
    dist = [max_num]*(N+1)
    dist[0] = 0 # 시작은 0으로 둔다
    for start in range(N+1):

        for i in range(N+1):
            if not visited[i] and dist[i] < dist[start]:
                start = i
        visited[start] = 1

        for i in range(N+1):
            if matrix[start][i]:
                dist[i] = min(dist[i], dist[start] + matrix[start][i])
                # print(dist)

    ans = dist[N]
    print('#{} {}'.format(tc, ans))