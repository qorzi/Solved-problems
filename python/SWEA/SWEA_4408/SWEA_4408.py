import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    return_room_lst = [list(map(int, input().split())) for _ in range(N)]

    # 룸에 경로 저장
    room_lst = [0]*400
    for i in range(N):
        for j in range(2):
            room_lst[return_room_lst[i][j]] = i+1

    # 공실을 지우고 루트 도출
    # [0, 1, 1, 0, 0, 3, 2, 0, 2, 3] -> [1, 1, 3, 2, 2, 3] -> '113223'
    while 0 in room_lst:
        room_lst.remove(0)
    # 형변환
    room_str = ''.join(list(map(str, room_lst)))

    # 이동 범위가 나머지의 범위와 충돌하지 않으면 삭제.
    # '11223344' -> ''  / '112332' -> '22' / 1212 -> 1212
    min_cnt = 0
    while room_str:
        min_cnt += 1
        for i in range(1, N+1):
            tmp_str = str(i)+str(i)
            if tmp_str in room_str:
                room_str = room_str.replace(tmp_str, '')

    # 겹치는 범위는?....



    print(f'#{tc} {min_cnt}')