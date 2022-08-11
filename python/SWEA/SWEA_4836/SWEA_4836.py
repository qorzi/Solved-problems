import sys
sys.stdin = open('input_4836.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # r1, c1, r2, c2, color

    #레드와 블루가 각각 존재하는 인덱스를 따로 담는다.
    # 리스트 내부에 인덱스 좌표를 튜플로 담어야 나중에 비교 간단
    red_index = [] #color 1
    blue_index = [] #color 2
    for i in range(N):
        for j in range(arr[i][2]-arr[i][0]+1):
            for k in range(arr[i][3]-arr[i][1]+1):
                if arr[i][4] == 1: #red
                    red_index += [(arr[i][0]+j, arr[i][1]+k)]
                elif arr[i][4] == 2: #blue
                    blue_index += [(arr[i][0]+j, arr[i][1]+k)]
    # print(red_index)
    # print(blue_index)
    #레드영역과 블루영역이 겹치는 곳 확인
    puple_index = []
    for i in red_index:
        for j in blue_index:
            if i == j:
                puple_index += [i]
    # print(puple_index)
    #중복 제거
    puple_index = set(puple_index)
    puple_index = list(puple_index)

    #갯수
    p_cnt = len(puple_index)

    print(f'#{tc} {p_cnt}')




