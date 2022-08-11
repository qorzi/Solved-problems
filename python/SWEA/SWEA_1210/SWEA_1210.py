import sys
sys.stdin = open('input_1210.txt', 'r')

for tc in range(1, 11):
    tc_N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    #도착점 구하기
    row = 0
    for i in range(100):
        if data[99][i] == 2:
            row = i

    column = 99
    while column > 0:
        #좌우
        if 0 <= row - 1 < 100 and data[column][row - 1] == 1:
            while data[column][row - 1] == 1:
                row -= 1
                if row == 0:
                    break
            column -= 1

        elif 0 <= row + 1 < 100 and data[column][row + 1] == 1:
            while data[column][row + 1] == 1:
                row += 1
                if row == 99:
                    break
            column -= 1

        else:
            column -= 1

        # print(column ,row)

    print(f'#{tc} {row}')


