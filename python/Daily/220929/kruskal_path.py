# SWEA 5249 최소신장트리 풀이
T = int(input())

def find_set(x):  # 효율성이 고려된 find set
    if p[x] != x:
        p[x] = find_set(p[x])  # path compression
    return p[x]


def union(x, y):  # 랭크가 고려 안된 union
    p[find_set(y)] = find_set(x)


for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])  # 가중치 오름차순 정렬
    p = [i for i in range(V+1)] # 시작은 자기 자신을 부모로 둔다

    answer = 0  # 가중치 합산 모아줄 변수
    cnt = 0  # 간선 선택 횟수

    for x, y, w in edges:  # 대표자 같으면 다음으로 걍 넘어감
        if find_set(x) != find_set(y):  # 대표자가 다른경우에만
            union(x, y)  # union 해주고
            answer += w  # 간선의 가중치를 합산
            cnt += 1  # 간선을 하나 사용했다고 체크

        if cnt == V:  # V-1 개까지만 선택해야 하니까!
            break

    print('#{} {}'.format(tc, answer))