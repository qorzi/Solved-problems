import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst.pop(0)

    go_cnt = 0
    change_cnt = -1
    bettery = 1
    keep = 0
    keep_cnt = 0
    while lst:
        go_cnt += 1
        bettery -= 1
        new_bettery = lst.pop(0)
        keep_cnt += 1

        # 남은 배터리가 이동 할 정거장 수보다 크다면, 이동
        if N - go_cnt <= bettery:
            continue

        # 경로를 이동하면서 해당 경로의 배터리를 일단 가지고 간다.
        # 가지고 다니는 배터리가 남은 경로보다 잔량이 많다면 바꾸지 않고
        # 남은 경로가 더 많다면, 배터리를 바꾼다.
        if keep - keep_cnt < N - go_cnt:
            if keep - keep_cnt < new_bettery:
                keep = new_bettery
                keep_cnt = 0

        # 기존에 장착하고 있는 배터리가 방전된다면,
        # 들고 다니는 배터리와 교환하는데, 이 배터리는 소지 시점부터 달고 있다.
        if bettery == 0:
            bettery = keep - keep_cnt
            change_cnt += 1

    print('#{} {}'.format(tc, change_cnt))
