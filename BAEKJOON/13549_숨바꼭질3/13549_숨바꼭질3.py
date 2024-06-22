from collections import deque

# sec 반환
def find_min_time(N, K):
    if N == K:
        return 0
    
    max_pos = 100000
    visited = [False] * (max_pos+1)
    queue = deque([(N, 0)]) # 위치, 시간

    while queue:
        pos, sec = queue.popleft()

        if pos == K:
            return sec
        
        # 순간이동
        if pos*2 <= max_pos and not visited[pos*2]:
            queue.append((pos*2, sec))
            visited[pos*2] = True
            
        # 걷기
        for dp in [-1, 1]:
            np = pos + dp
            if 0 <= np <= max_pos and not visited[np]:
                queue.append((np, sec+1))
                visited[np] = True

N, K = map(int, input().split()) # 시작 위치, 도착 위치(ex 5, 17)

res = find_min_time(N, K)
print(res)