import sys
sys.stdin = open('input_4836.txt', 'r')

#모든 경우에 부분 집합은 동일하기 때문에 한번만
all_subset = []
#요소는 총 12개
for i in range(1<<12):
    subset = []
    #12번 밀어야함
    for j in range(12):
        if i & (1<<j):
            #위에서 확인만 하고 있으면 +1 해서 원래 숫자로 맞춰줌
            subset += [j+1]
    all_subset += [subset]
# print(all_subset)

#이제 실행
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    ans = 0
    for i in all_subset:
        #요소 갯수 N개, 합이 K면
        if len(i) == N and sum(i) == K:
            ans += 1

    print(f'#{tc} {ans}')
