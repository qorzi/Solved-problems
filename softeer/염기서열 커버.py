import sys

N, M = map(int, input().split())

good_list = [list(input()) for _ in range(N)]

# 사용 가능한 최소 문자 조합 가져오기
min_list = []
for i in range(M):
    alphabet = []
    for j in range(N):
        if good_list[j][i] == ".":
            continue
        if good_list[j][i] not in alphabet:
            alphabet.append(good_list[j][i])
    min_list.append(alphabet)
