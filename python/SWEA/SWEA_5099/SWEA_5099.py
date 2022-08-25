import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    queue = [0]*N
    pizza_num_queue = [0]*N

    # 한바퀴 회전을 카운트 하기 위한 변수
    pizza_num = 0

    while lst or queue:

        # 비어 있으면 피자 채우기
        if pizza_num_queue[0] == 0 and lst:
            pizza_num += 1
            tmp = lst.pop(0)
            # 치즈 넘버 넣기
            queue.pop(0)
            queue.append(tmp)
            # 피자 넘버 넣기
            pizza_num_queue.pop(0)
            pizza_num_queue.append(pizza_num)
        else:
            tmp = queue.pop(0)//2
            tmp_num = pizza_num_queue.pop(0)
            # 치즈가 다 녹았다면, 새거 넣기
            if tmp == 0:
                ans = tmp_num
                # 피자가 남아 있다면,
                if lst:
                    # 피자 다시 넣기
                    pizza_num += 1
                    tmp = lst.pop(0)
                    queue.append(tmp)
                    pizza_num_queue.append(pizza_num)
            # 치즈가 덜 녹았다면, 다시 넣기
            else:
                queue.append(tmp)
                pizza_num_queue.append(tmp_num)
        # print(queue, pizza_num_queue)
    print(f'#{tc} {ans}')