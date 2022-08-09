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

    #한번에 갈 수 있는 경우,
    if charged_run >= end_stop:
        go_bus = False

    # 계산을 위한 리스트 확장
    for i in range(charged_run):
        charging_spot.insert(0, 0)  # 인덱스 0에 추가
        charging_spot.append(0)  # 인덱스 마지막에 추가

    #충전 횟수 계산
    while go_bus:
        now_spot = 0
        for i in range(charged_run, len(charging_spot)-charged_run):
            print(i)

            #종착역에 도착하거나 넘으면 끝
            if now_spot + charged_run >= end_stop:
                # print('도착')
                go_bus = False
                break
            #K만큼 이동하고 충전소일 때
            elif now_spot + charged_run in charging_spot:
                # print('K만큼')
                now_spot += charged_run
                min_charging_cnt += 1
            #K만큼 이동이 충전소가 아닐 때, 먼 곳으로
            elif now_spot + charged_run > charging_spot[i]:
                # print('K보다 덜')
                for j in range(len(charging_spot)-charged_run-1, i-1, -1):
                    print(charging_spot[j], charging_spot[i], j)
                    if charging_spot[j] - now_spot == charged_run:
                        print('same')
                        now_spot += charged_run
                        min_charging_cnt += 1
                        break
                    elif charging_spot[j] - now_spot < charged_run:
                        print('down')
                        now_spot += j - i + 1
                        min_charging_cnt += 1
                        break
            # print(min_charging_cnt, now_spot)

        else:
            break

    #test_count, 최소 충전 횟수
    print(f'#{test_count} {min_charging_cnt}')