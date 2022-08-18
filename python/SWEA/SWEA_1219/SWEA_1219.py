import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc, lst_cnt = map(int, input().split())
    lst = list(map(int, input().split()))
    # print(lst)
    adj_matrix = [[0]*(100) for _ in range(100)]
    for i in range(lst_cnt):
        start = lst[i*2]
        end = lst[i*2+1]
        # print(start, end)
        adj_matrix[start][end] = 1

    stack = [0]
    visited = []

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)

        for destination in range(100):
            if destination not in visited and adj_matrix[current][destination]:
                stack.append(destination)

    # print(visited)
    ans = 0
    if 99 in visited:
        ans = 1

    print(f'#{tc} {ans}')

