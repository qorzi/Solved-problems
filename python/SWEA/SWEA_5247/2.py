import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0]*(M+11)*2 # not in은 느리니까, 0과 M+10을 고려해서 보다 크게 설정
    visited_num = (M+11)*2
    total = []
    cnt = -1
    ans = 0

    start = [[N, cnt]]
    while start:
        # print('start', start)
        current = start.pop(0)
        cnt = current.pop()
        cnt += 1
        current_num = len(current)
        # print('->', current, '카운트', cnt)
        for _ in range(current_num):
            tmp = []
            now = current.pop(0)
            if visited[now]:
                continue
            visited[now] = 1
            # print('visited', now, '->', visited)

            if now == M: # 목표값에 도달 했으면 루프에서 나오기
                ans = cnt
                start = []
                break

            # d -> +1, -1, *2, -10
            for j in range(4):
                if j == 0:
                    go = now + 1
                elif j == 1:
                    go = now - 1
                elif j == 2:
                    go = now * 2
                elif j == 3:
                    go = now - 10

                if 1 <= go < visited_num and visited[go] == 0:
                    tmp.append(go)
            if tmp:
                tmp = list(set(tmp)) # 중복 제거
                tmp.append(cnt)
                # print(now, '경로', tmp,'마지막은 카운트')
                start.append(tmp)

    print('#{} {}'.format(tc, ans))