N, d, k, c = map(int, input().split())  # 접시 수, 초밥의 종류, 연속 접시 수, 쿠폰 번호
dishes = [int(input()) for _ in range(N)]
dishes.extend(dishes[:k-1])
max_kinds = 0

for i in range(N):
    current = dishes[i: i + k]
    have = [0] * (d +1)
    kinds = 0
    for j in current:
        if have[j] == 0:
            kinds += 1
        have[j] += 1
    kinds += (1 if have[c] == 0 else 0)
    max_kinds = max(kinds, max_kinds)

print(max_kinds)   
