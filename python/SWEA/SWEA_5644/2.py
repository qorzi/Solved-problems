import sys
sys.stdin = open('sample_input.txt', 'r')

# 해당 좌표에서 연동 가능 한 ap를 찾는 함수
def detect_ap(i, j):
    tmp = []
    for n in range(N):
        D = abs(ap[n][0]-i) + abs(ap[n][1]-j)
        if D <= ap[n][2]:
            tmp += [ap[n][3]]
        else:
            tmp += [0]
    return tmp

# 방향 저장
direct = {0: [0, 0], 1: [-1, 0], 2: [0, 1], 3: [1, 0], 4: [0, -1]}
T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split())
    user_move = [[0]+list(map(int, input().split())) for _ in range(2)]
    # i, j, 거리, 파워
    ap = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 인덱스에 맞춰 인덱스 재조정
    for i in range(N):
        ap[i][0] -= 1
        ap[i][1] -= 1
        ap[i][0], ap[i][1] = ap[i][1], ap[i][0]
    # 성능이 좋은 ap가 앞에 오도록 한다.
    ap.sort(key=lambda x: -x[3])

    # 유저 정보
    user_info = [[0,0], [9,9]]
    # 시작위치도 순회
    for i in range(M+1):
        can_ap = []
        for user in range(2):
            di, dj = direct[user_move[user].pop(0)]
            user_info[user][0] += di
            user_info[user][1] += dj
            can_ap += [detect_ap(user_info[user][0], user_info[user][1])]
        # 생각해보면 총합을 구하는 것이 때문에 충전기가 겹칠 경우, 한 곳만 더하면 된다.
        charger_visited = [0] * N
        charger_visited_2 = [0] * N
        # A, B 가 이미 충전됬는지 확인하는 스위치
        A = B = 1
        C = D = 1
        tmp_A = tmp_B = 0
        for j in range(N):
            # 0번 유저 선 순회
            if can_ap[0][j] and charger_visited[j] == 0 and A:
                tmp_A += ap[j][3]
                charger_visited[j] = 1
                A = 0
            elif can_ap[1][j] and charger_visited[j] == 0 and B:
                tmp_A += ap[j][3]
                charger_visited_2[j] = 1
                B = 0
            # 1번 유서 선 순회
            if can_ap[1][j] and charger_visited_2[j] == 0 and C:
                tmp_B += ap[j][3]
                charger_visited[j] = 1
                C = 0
            elif can_ap[0][j] and charger_visited_2[j] == 0 and D:
                tmp_B += ap[j][3]
                charger_visited_2[j] = 1
                D = 0

        ans += max(tmp_A, tmp_B)

    print('#{} {}'.format(tc, ans))