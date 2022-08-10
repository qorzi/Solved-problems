import sys
sys.stdin = open('input_1954.txt')
T = int(input())
# T = 1

for tc in range(1, T+1):
    N = int(input())
    # N = 4
    box = [[0]*N for _ in range(N)]
    start_cnt = 1

    #홀수
    if N % 2:
        inner_box_cnt = int((N+1)/2)
    #짝수
    elif not N % 2:
        inner_box_cnt = int(N/2)
        
    #기준점 찾기 (0,0) -> (1,1) ...
    #매 사이클 시작점 [i][i]
    for i in range(inner_box_cnt):
        start_point = i
        reverse_point = N - i - 1

        if start_point == reverse_point:
            box[start_point][start_point] = start_cnt
            start_cnt += 1
        else:
            #각 기준점에서 N-1-i*2회 씩, 4번 이동
            #내부 사각형에서 한줄에 이동하는 칸 수
            move_cnt = N-1-i*2
            
            #좌표 리스트
            dx = [0]*4*(move_cnt)
            dy = [0]*4*(move_cnt)

            #좌표 설정
            for k in range(move_cnt):
                dx[k] = start_point
                dy[k] = start_point + k
                dx[move_cnt + k] = start_point + k
                dy[move_cnt + k] = reverse_point
                dx[move_cnt*2 + k] = reverse_point
                dy[move_cnt*2 + k] = reverse_point - k
                dx[move_cnt*3 + k] = reverse_point - k
                dy[move_cnt*3 + k] = start_point
                    
            for j in range(move_cnt*4):
                box[dx[j]][dy[j]] = start_cnt
                start_cnt += 1
    
    print(f'#{tc}')
    for innerbox in box:
        print(*innerbox)