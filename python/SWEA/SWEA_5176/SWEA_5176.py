import sys
sys.stdin = open('sample_input.txt', 'r')
def inorder(n):
    global tree
    global cnt
    if n <= N:
        # print(n, 2*n, 2*n+1)
        inorder(2*n)
        # print(n)
        tree[n] = cnt
        cnt += 1
        inorder(2*n+1)
        # print('return')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)

# 1 2 4 8 16 ...
    depth = 0
    while N < 2**(depth+1):
        depth += 1

    start = 1

    # print('----')
    cnt = 1
    inorder(1)
    # print(tree)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))