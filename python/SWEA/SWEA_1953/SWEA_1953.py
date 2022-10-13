import sys
sys.stdin = open('sample_input.txt', 'r')

# 두 가려는 곳의 터널과 현재 터널이 연결 되어 있는가?
def connect(direct, i, j, di, dj):
    tunnel_destination = tunnels[matrix[i+di][j+dj]]

    for direct_destination in tunnel_destination:
        if direct == 'up' and direct_destination[0] == 'down':
            return True
        elif direct == 'down' and direct_destination[0] == 'up':
            return True
        elif direct == 'left' and direct_destination[0] == 'right':
            return True
        elif direct == 'right' and direct_destination[0] == 'left':
            return True
    return False


# 각 터널 번호별로 갈 수 있는 방향 지정해주기 - 딕셔너리 활용
tunnels = {1: (('up', -1, 0), ('down', 1, 0), ('left', 0, -1), ('right', 0, 1)),
           2: (('up', -1, 0), ('down', 1, 0)),
           3: (('left', 0, -1), ('right', 0, 1)),
           4: (('up', -1, 0), ('right', 0, 1)),
           5: (('down', 1, 0), ('right', 0, 1)),
           6: (('down', 1, 0), ('left', 0, -1)),
           7: (('up', -1, 0), ('left', 0, -1))}

T = int(input())
for tc in range(1, T+1):
    N, M, start_i, start_j, time = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    start = [[(start_i, start_j)]]

    cnt = 0
    while cnt != time and start:
        # print('start', start)
        cnt += 1
        current = start.pop(0)
        tmp = []
        while current:
            i, j = current.pop(0)
            # print(i, j)

            if visited[i][j]:
                continue
            visited[i][j] = cnt

            tunnel = tunnels[matrix[i][j]]
            for diret, di, dj in tunnel:
                if 0 <= i+di < N and 0 <= j+dj < M and matrix[i+di][j+dj] and visited[i+di][j+dj] == 0:
                    if connect(diret, i, j, di, dj): # 서로 연결 되어 있는지
                        tmp.append((i+di, j+dj))

        if tmp:
            # print('tmp', tmp)
            start.append(tmp)

        # print(*visited, sep='\n')

    ans = 0
    for a in range(N):
        for b in range(M):
            if visited[a][b]:
                ans += 1
    print('#{} {}'.format(tc, ans))