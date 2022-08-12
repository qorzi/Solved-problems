import sys
sys.stdin = open('input_4865.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    #문자열 끊어서 리스트로 받기
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))

    #리스트 돌려서 갯수 가져오기
    cnt_list = []
    for i in str1:
        str_cnt = 0
        for j in str2:
            if i == j:
                str_cnt += 1
        cnt_list += [str_cnt]

    #최대값 구하기
    max_cnt = 0
    for i in cnt_list:
        if i > max_cnt:
            max_cnt = i

    print(f'#{tc} {max_cnt}')
