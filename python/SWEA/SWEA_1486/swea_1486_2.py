import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, 1+1):
    N, B = map(int, input().split())
    h_lst = list(map(int, input().split()))

    #부분집합 구하기
    subsets = [[]]
    for i in h_lst:
        size = len(subsets)
        for j in range(size):
            subsets += [[i] + subsets[j]]
    print(subsets)