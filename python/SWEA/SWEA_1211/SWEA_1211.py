import sys
sys.stdin = open('input (1).txt', 'r')

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    start = []
    for i in range(100):
        if ladder[0][i] == 1:
            start.append([0, i])
    # print(start)

    min_int = 100 * 100
    while start:
        r, c = start.pop(0)
        start_c = c

        step = 0
        while r < 100:
            if c+1 < 100 and ladder[r][c+1] == 1:
                while c+1 < 100 and ladder[r][c+1] == 1:
                    c += 1
                    step += 1
                r += 1
                step += 1
            elif 0 <= c-1 and ladder[r][c-1] == 1:
                while 0 <= c-1 and ladder[r][c-1] == 1:
                    c -= 1
                    step += 1
                r += 1
                step += 1
            else:
                r += 1
                step += 1

        if step < min_int:
            min_int = step
            ans = start_c

    print(f'#{tc} {ans}')
