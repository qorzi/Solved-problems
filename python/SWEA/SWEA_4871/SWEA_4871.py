import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_matrix = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        adj_matrix[start][end] = 1

    S, G = map(int, input().split())
    stack = [S]
    visited = []

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)

        for destination in range(V+1):
            if adj_matrix[current][destination] and destination not in visited:
                stack.append(destination)

    ans = 0
    if G in visited:
        ans = 1
    # print(S, G)
    # print(visited)

    print(f'#{tc} {ans}')