import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    cnt_s = 0
    start = M
    cnt_e = 0
    end = N

    print(start)
    while start:
        if start == end + 1:
            start -= 1
            cnt_s += 1
            print(start)
            break
        elif start == end:
            print(start)
            break

        if start%2 and start-1 >= end:
            start -= 1
            cnt_s += 1
            print(start)
        if start//2 > start - 10 and start - 10 >= end:
            start -= 10
            cnt_s += 1
        else:
            start = start//2
            cnt_s += 1
        print(start)
    print('카운트',cnt_s)
    print('---')
