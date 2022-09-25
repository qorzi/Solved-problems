import sys
sys.stdin = open('input (1).txt', 'r')

for tc in range(1, 11):
    N, start = map(int, input().split())
    lst = list(map(int, input().split()))
    max_num = max(lst)+1
    route = [[0]*max_num for _ in range(max_num)]
    visited = [0]*max_num
    ans = 0

    size = len(lst)//2
    for i in range(size):
        route[lst[i*2]][lst[i*2+1]] = 1

    queue = [[start]]
    while queue:
        current_lst = queue.pop(0)
        size = len(current_lst)
        go_visit = []
        for _ in range(size):
            current = current_lst.pop(0)
            if visited[current]:
                continue
            visited[current] = 1

            for next in range(max_num):
                if not visited[next] and route[current][next]:
                    go_visit += [next]

            if go_visit:
                ans = max(go_visit)
                queue.append(go_visit)

    print('#{} {}'.format(tc, ans))