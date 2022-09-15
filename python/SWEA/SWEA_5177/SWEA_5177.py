import sys
sys.stdin = open('sample_input.txt', 'r')

def enq(n):
    global last
    last += 1 # 마지막 정점 추가
    heap[last] = n # 마지막 정점에 key 추가
    # 부모 > 자식 인경우 자리 교환 (부모가 없거나 부모 < 자식 조건을 만족 할 때까지)
    c = last
    p = c//2 # 완전이진트리에서 부모 정점 번호
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

def sum_root(n):
    global rootsum
    n = n//2
    if heap[n]:
        rootsum += heap[n]
        sum_root(n)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N_lst = list(map(int, input().split()))

    heap = [0] * (N+1)
    last = 0
    for i in N_lst:
        enq(i)
    # print(heap)

    rootsum = 0
    sum_root(N)
    print('#{} {}'.format(tc, rootsum))