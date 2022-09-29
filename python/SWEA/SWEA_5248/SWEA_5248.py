import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    matrix = [[0]*(N+1) for _ in range(N+1)]
    visited = [0]*(N+1)

    num = len(lst)//2
    for i in range(num):
        matrix[lst[i*2]][lst[i*2+1]] = 1
        matrix[lst[i*2+1]][lst[i*2]] = 1

    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            start = [i]
            cnt += 1
            while start:
                current = start.pop()
                if visited[current]:
                    continue
                visited[current] = 1
                for destination in range(1, N+1):
                    if matrix[current][destination] and visited[destination] == 0:
                        start.append(destination)


    print('#{} {}'.format(tc, cnt))