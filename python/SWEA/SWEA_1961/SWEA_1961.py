import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    line = int(input())
    matrix = [list(map(int, input().split())) for _ in range(line)]

    #zip으로 90회전 회전 회전
    rota_90 = list(map(list, zip(*matrix[::-1])))
    rota_180 = list(map(list, zip(*rota_90[::-1])))
    rota_270 = list(map(list, zip(*rota_180[::-1])))

    #프린트 정리
    print(f'#{tc}')
    for i in range(line):
        for j in range(line):
            print(rota_90[i][j], end='')
        print(' ', end='')
        for j in range(line):
            print(rota_180[i][j], end='')
        print(' ', end='')
        for j in range(line):
            print(rota_270[i][j], end='')
        print('')
