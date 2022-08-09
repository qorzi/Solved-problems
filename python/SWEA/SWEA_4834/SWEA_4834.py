import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tester in range(T):
    N = int(input())
    num = list(map(int, input()))
    # print(num)

    #카운팅
    cnt_list = [0]*10

    for i in range(0, N):
        cnt_list[num[i]] += 1
    # print(cnt_list)

    #최대 개수
    max_cnt = 0
    for i in cnt_list:
        if i > max_cnt:
            max_cnt = i
    # print(max_cnt)

    #큰 수를 뽑기 위해 리버스
    cnt_list.reverse()

    print(f'#{tester+1} {9-cnt_list.index(max_cnt)} {max_cnt}')