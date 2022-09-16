import sys
sys.stdin = open('input (1).txt', 'r')

T = 10
for tc in range(1, 11):
    N, start = map(int, input().split())
    lst = list(map(int, input().split()))

    Max_num = max(lst)
    matrix = [[0]*(Max_num+1) for _ in range(Max_num+1)]
    visited = []

    for i in range(N//2):
        i, j = lst[2*i], lst[2*i+1]
        matrix[i][j] = 1

    queue = [[start]]

    while queue:

        current_lst = queue.pop(0)
        size = len(current_lst)
        tmp = []
        for _ in range(size):
            current = current_lst.pop(0)
            if current not in visited:
                visited.append(current)

            for destination in range(Max_num+1):
                if matrix[current][destination] and destination not in visited:
                    tmp.append(destination)
        if tmp:
            queue.append(tmp)

            ans_lst = []
            for i in tmp[:]:
                if i not in visited:
                    ans_lst.append(i)
                    if ans_lst:
                        ans = max(ans_lst)


    print('#{} {}'.format(tc, ans))

