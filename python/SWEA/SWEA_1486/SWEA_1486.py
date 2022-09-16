import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    # 부분집합 합
    subsets = [0]
    for num in lst:
        size = len(subsets)
        for i in range(size):
            subsets.append(subsets[i] + num)

    # 최저 차
    ans = 10000
    for i in subsets:
        tmp = i-B
        if 0 <= tmp < ans:
            ans = tmp

    print('#{} {}'.format(tc, ans))