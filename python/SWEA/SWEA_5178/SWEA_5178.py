import sys
sys.stdin = open('sample_input.txt', 'r')

def sum_leaf(n):
    if n <= N:
        # print('here',n)
        sum_leaf(n*2)
        sum_leaf(n*2+1)
        if not node[n]:
            # print(n,'empty')
            if n*2 <= N and n*2+1 <= N:
                if node[n*2] and node[n*2+1]:
                    node[n] = node[n*2] + node[n*2+1]
            elif n*2 <= N:
                if node[n*2]:
                    node[n] = node[n * 2]
        # print(node)

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    node = [0]*(N+1)
    for _ in range(M):
        i, j = map(int, input().split())
        node[i] = j

    sum_leaf(1)
    print('#{} {}'.format(tc, node[L]))
    # print('---')