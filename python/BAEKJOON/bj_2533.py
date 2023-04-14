from collections import deque

V = int(input())

# 인접 리스트
adj_list = [[] for _ in range(V+1)]

for _ in range(V-1):
    start, end = map(int, input().split())
    adj_list[start].append(end)
    adj_list[end].append(start)

parent = [0] * (V+1)
visited = set()
child_cnt = [0] * (V+1)
leaves = set()
queue = deque()

stack = [1]

# 트리 만들기
while stack:
    current = stack.pop()
    if current in visited:
        continue

    visited.add(current)

    for destination in adj_list[current]:
        if destination not in visited:
            parent[destination] = current  # 현재 노드의 부모를 기록한다
            stack.append(destination)
            child_cnt[current] += 1

    if not child_cnt[current]:
        leaves.add(current)  # 리브 노드인지 기록
        queue.append(current)  # 리브에서 탐색을 시작하기 위해 추가

# 얼리어답터 노드들
early_nodes = set()

# 리브노드에서 시작
while queue:
    current = queue.popleft()

    # 현재 노드가 얼리어답터가 아니면 내 부모 노드는 무조건 얼리어답터로 추가
    if current not in early_nodes:
        early_nodes.add(parent[current])

    # 자식 노드를 모두 봤다면 queue에 추가
    child_cnt[parent[current]] -= 1  # 현재 노드의 부모가 가진 수 -= 1
    if not child_cnt[parent[current]]:  # 현재 노드의 부모의 남은 자식이 없다면
        if parent[current] == 0:  # 부모가 없다면(루트 노드라면)
            continue
        queue.append(parent[current])

print(len(early_nodes))
