# # 방법 1
# N, M = map(int, input().split())
# adj_lst = [[] for _ in range(N)]

# min_num = 0

# for num in range(1, M+1):
#     # 경로 추가
#     i, j = map(int, input().split())
#     adj_lst[i].append(j)
#     adj_lst[j].append(i)

#     stack = [(i, None)]  # 시작 정점과 이전 정점을 저장
#     visited = set()

#     if min_num:  # 최소 경로를 찾았으면 skip
#         continue

#     while stack:
#         current, previous = stack.pop()

#         if current in visited:
#             continue

#         visited.add(current)

#         for destination in adj_lst[current]:
#             if destination != previous and destination == i:
#                 min_num = num
#                 break

#             # 이전 정점으로의 이동을 제한
#             if destination != previous and destination not in visited:
#                 stack.append((destination, current))

# print(min_num)


# 방법 2
def find(x):
    # 루트 노드를 찾을 때까지 반복
    while x != parent[x]:
        x = parent[x]
    return x


def union(x, y):
    x = find(x)
    y = find(y)
    # 만약 x와 y가 다른 집합에 속해 있다면, y의 root 노드를 x로
    if x != y:
        parent[y] = x


n, m = map(int, input().split())
parent = list(range(n))
cycle = 0

# 각 차례에 대해
for i in range(1, m+1):

    a, b = map(int, input().split())

    # 사이클이 형성되었으면 skip
    if cycle:
        continue

    if find(a) == find(b):
        # 현재 차례를 저장
        cycle = i

    else:
        union(a, b)

print(cycle)
