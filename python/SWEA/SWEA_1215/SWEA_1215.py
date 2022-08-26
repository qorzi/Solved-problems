import sys
sys.stdin = open('input.txt', 'r')

def detect(matrix):
    global cnt
    for i in range(8):
        for j in range(8-N+1):
            tmp = matrix[i][j:j+N]
            if tmp == tmp[::-1]:
                cnt += 1



for tc in range(1, 11):
    N = int(input())
    matrix = [list(map(str, input())) for _ in range(8)]
    # print(matrix)
    cnt = 0
    detect(matrix)
    matrix_90 = list(map(list, zip(*matrix[::-1])))
    # print(matrix_90)
    detect(matrix_90)

    print(f'#{tc} {cnt}')
