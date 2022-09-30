import sys
sys.stdin = open('sample_input.txt', 'r')

# 해당 좌표에서 연동 가능 한 ap를 찾는 함수
def detect_ap(i, j):
    tmp = []
    for n in range(A):
        D = abs(ap[n][0]-i) + abs(ap[n][1]-j)
        if D <= ap[n][2]:
            tmp += [1]
        else:
            tmp += [0]
    return tmp

# 어느 ap에 연결해야 할 지 최적화 및 충전
def distribute_ap():
    distribute_dt = True # 기본 값 분배 가능
    flag = False # 순회 파괴용
    # 차지 파워가 큰 순으로 순회
    for i in range(A):
        # 동시 접속이 가능할 때,
        if user_can_ap[0][i]:
            if user_can_ap[0][i] == user_can_ap[1][i]:
                distribute_dt = False
                for j in range(A):
                    # 또 다른 접속 연결 단자가 존재한다면, 이전 접속 제거
                    if i != j:
                        if user_can_ap[0][j]:
                            user_can_ap[0][i] = 0
                            distribute_dt = True
                        elif user_can_ap[1][j]:
                            user_can_ap[1][i] = 0
                            distribute_dt = True
                        # 상위 차저만 사용 할거니 이후 필요 X
                        flag = True
                        break
        if flag:
            break
    return distribute_dt

def charging(distribute_dt):
    # 분배가 가능할 때, 처음 선택 된 것을 충전
    if distribute_dt:
        A_on = B_on = True
        for i in range(A):
            if user_can_ap[0][i] and A_on:
                user_info[0][2] += ap[i][3]
                A_on = False
            if user_can_ap[1][i] and B_on:
                user_info[1][2] += ap[i][3]
                B_on = False
            if A_on == False and B_on == False:
                break

    # 충전기 분배가 불가능한 경우, 파워를 나눠 충전
    else:
        for i in range(A):
            if user_can_ap[0][i]:
                if user_can_ap[0][i] == user_can_ap[0][i]:
                    user_info[0][2] += ap[i][3]//2
                    user_info[1][2] += ap[i][3]//2

# 방향 저장
direct = {0: [0, 0], 1: [-1, 0], 2: [0, 1], 3: [1, 0], 4: [0, -1]}
T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split()) # 이동시간, 충전기 갯수
    user_A_route = [0] + list(map(int, input().split()))
    user_B_route = [0] + list(map(int, input().split()))
    user_route_matrix = [user_A_route, user_B_route]

    # i, j, 거리, 성능
    ap = [list(map(int, input().split())) for _ in range(A)]
    # 인덱스에 맞춰 위치 재조정
    for i in range(A):
        ap[i][0] -= 1
        ap[i][1] -= 1
        ap[i][0], ap[i][1] = ap[i][1], ap[i][0]
    # 성능이 좋은 ap가 앞에 오도록 한다.
    ap.sort(key= lambda x: -x[3])
    print(ap)

    user_info = [[0, 0, 0], [9, 9, 0]]
    for i in range(M+1):
        # 유저 좌표 이동 및 ap 탐색 및 ap 탐색
        user_can_ap = []
        for user in range(2):
            di, dj = direct[user_route_matrix[user].pop(0)]
            user_info[user][0] += di
            user_info[user][1] += dj
            user_can_ap += [detect_ap(user_info[user][0], user_info[user][1])]
        print(user_can_ap)
        # 분배 가능 판단
        distribute_dt = distribute_ap()
        print(user_can_ap)
        print(distribute_dt)
        # 충전
        charging(distribute_dt)
        print(user_info)

    ans = user_info[0][2] + user_info[1][2]

    print('#{} {}'.format(tc, ans))


