import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 90도 회전시, 좌측이 S 우측이 N
    matrix_90 = list(map(list, zip(*matrix[::-1])))

    # 행렬내 0 제거, N극 자성체(1) 좌측에서 제거, S극 자성체(2) 우측에서 제거
    # 예) [0, 1, 0, 0, 2, 0, 1, 1, 2] -> [2, 1, 1]
    for i in range(100):
        while 0 in matrix_90[i]:
            matrix_90[i].remove(0)
        while matrix_90[i][0] == 1:
            matrix_90[i].pop(0)
        while matrix_90[i][-1] == 2:
            matrix_90[i].pop()

    # # 연속 된 '21' -> '3' 변경후, count('3')의 수를 반환
    str_list = []
    ans = 0
    for i in range(100):
        str_list += [''.join(list(map(str, matrix_90[i])))]
        str_list[i] = str_list[i].replace('21', '3')
        ans += str_list[i].count('3')

    print(f'#{tc} {ans}')