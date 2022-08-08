import sys
sys.stdin = open('input.txt')

# 10가지의 경우에 대해 입력을 받는다.
for cnt in range(10):
    #땅의 범위
    ground = int(input())
    #빌딩들의 층수
    buildings = list(map(int, input().split()))

    #문제 풀이 방법
    #인접 두 칸의 빌딩 들과 층수를 뺄셈하여, 그 값이 최소가 되는 녀석들은 조망권이 확보된다.
    #1. 인접 두 칸과의 뺄셈들의 리스트를 확보한다.
    #현재 빌딩과 앞뒤로 2칸까지의 조망권을 계산해 담는다.
    good_sight_list = []
    for i in range(2, ground-2):
        tmp_list = []
        for j in [-2, -1, 1, 2]:
            if (buildings[i] - buildings[i+j]) >= 0:
                tmp_list += [buildings[i] - buildings[i+j]]
            #현재 위치 보다 높은 건물이 존재할 경우, 조망권 없음
            else :
                tmp_list += [0]
        # print(tmp_list)
        #2. 리스트의 값 중 최소가 되는 값을 고른다.
        #조망권이 가장 낮은 경우의 수를 저장
        tmp_row = 256
        for k in tmp_list:
            if k <= tmp_row:
                tmp_row = k
        if tmp_row != 256:
            # print(tmp_row)
            good_sight_list += [tmp_row]
    # print(good_sight_list)
    #3. 최소값들을 모두 더해 조망권이 확도된 총 세대수를 추출한다.
    #모든 조망권의 수를 합하여 저장
    all_good_sight_counts = 0
    for l in good_sight_list:
        all_good_sight_counts += l

    print(f'#{cnt+1} {all_good_sight_counts}')