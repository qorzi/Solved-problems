from collections import defaultdict

n = int(input())
if n == 1:
    print(1)
else:
    parents = list(map(int, input().split()))
    tree = defaultdict(list)

    for i, parent in enumerate(parents, start=2):
        tree[parent].append(i)

    # tree 딕셔너리에서 자식 수가 최대인 경우를 찾는다.
    companies = max(len(children) for children in tree.values())

    print(companies)
