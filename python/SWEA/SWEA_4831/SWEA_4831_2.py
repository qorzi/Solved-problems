import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_count in range(1, T+1):
    charged_run, end_stop, charging_spot_cnt = map(int, input().split())
    charging_spot = list(map(int, input().split()))

    go_bus = True
    min_charging_cnt = 0

    #charged_run칸 내에 다음 충전소가 없는 경우,
    charging_spot.insert(0, 0) #시작점 추가
    for i in range(len(charging_spot) - 1):
        if charging_spot[i + 1] - charging_spot[i] > charged_run:
            go_bus = False
            break
    charging_spot.pop(0) #사용 후, 제거

    #버스 출발
    now_spot = 0
    while go_bus:

        #종착역에 도착 + 한번에 갈 수 있는 경우
        if now_spot + charged_run >= end_stop:
            break

        #갈 수 있는 가장 먼 충전소
        max_spot = 0
        for i in charging_spot:
            if i <= now_spot + charged_run:
                max_spot = i

        min_charging_cnt += 1
        now_spot = max_spot

    print(f'#{test_count} {min_charging_cnt}')
