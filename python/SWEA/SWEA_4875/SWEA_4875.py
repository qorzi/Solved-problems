import sys
sys.stdin = open('sample_input.txt', 'r')

def maze(y, x):
    global ans
    global visited
    global nopass

    print(y, x)
    # 지나감 표시
    visit = [y, x]
    visited += [visit[:]]
    print('visited', visited)

    # 도착-이미 값이 나왔다면 리턴, 남은 길이 없다면 리턴
    if ans or nopass:
        return
    if matrix[y][x] == 3:
        # print('도착')
        ans = 1
        return

    #갈 수 있고 + 방문한 적 없는 곳
    #오른쪽
    if 0 <= y < N and 0 <= x+1 < N:
        if matrix[y][x+1] == 0 or matrix[y][x+1] == 3:
            if [y, x+1] not in visited:
                divide_root_keep.append([y, x+1])
    #왼쪽
    if 0 <= y < N and 0 <= x-1 < N:
        if matrix[y][x-1] == 0 or matrix[y][x-1] == 3:
            if[y, x-1] not in visited:
                divide_root_keep.append([y, x-1])
    #아래
    if 0 <= y+1 < N and 0 <= x < N:
        if matrix[y+1][x] == 0 or matrix[y+1][x] == 3:
            if not [y+1, x] in visited:
                divide_root_keep.append([y+1, x])
    #위
    if 0 <= y-1 < N and 0 <= x < N:
        if matrix[y-1][x] == 0 or matrix[y-1][x] == 3:
            if [y-1, x] not in visited:
                divide_root_keep.append([y-1, x])

    #갈 수 있는 경로가 없다면 리턴
    if not divide_root_keep:
        # print('리턴')
        nopass = 1
        return

    # print('divide', divide_root_keep)
    #길이 막히면 아까 갈림길에서 다른 경로로 가짐.
    y, x = divide_root_keep.pop()
    maze(y, x)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    #시작 포인트 설정
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                x = j
                y = i

    #[y, x]로 저장
    divide_root_keep = []
    visited = []
    ans = 0
    nopass = 0

    maze(y, x)

    print(f'#{tc} {ans}')