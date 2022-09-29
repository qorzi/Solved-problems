import sys
sys.stdin = open('sample_input.txt', 'r')

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    e_lst = [list(map(int, input().split())) for _ in range(E)]
    e_lst.sort(key=lambda x: x[2])
    p = [i for i in range(V+1)]

    ans = 0
    cnt = 0 # V-1 까지

    for x, y, w in e_lst:
        if find_set(x) != find_set(y):
            union(x, y)
            ans += w
            cnt += 1

        if cnt == V:
            break

    print('#{} {}'.format(tc, ans))
