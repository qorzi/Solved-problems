import sys
sys.stdin = open('sample_input.txt', 'r')

def truck(m):
    global max_weight
    global visited_N
    n_max = 0
    for n in N_lst:
        if n <= m and n > n_max:
            n_max = n

    if n_max:
        N_lst.remove(n_max)
        max_weight += n_max

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_lst = list(map(int, input().split()))
    M_lst = list(map(int, input().split()))

    max_weight = 0
    for m in M_lst:
        truck(m)
    print('#{} {}'.format(tc, max_weight))