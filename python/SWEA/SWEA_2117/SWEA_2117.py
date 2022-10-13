import sys
sys.stdin = open('sample_input.txt', 'r')

def operating_cost(K): # K일 때 비용
    return K**2+(K-1)**2

def client_service_money(i, j, K, cnt): # 수입
    for a in range(-K+1, K):
        for b in range(-K+1, K):
            if abs(a)+abs(b) < K:
                if 0<=i+a<N and 0<=j+b<N:
                    if matrix[i+a][j+b]:
                        cnt += 1

    return M*cnt, cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_house = 0
    for k in range(1, N+2):
        for i in range(N):
            for j in range(N):
                a = operating_cost(k)
                b, house_num = client_service_money(i, j, k, 0)
                if b >= a: # 수입이 더 크거나 같을 때
                    if max_house < house_num:
                        max_house = house_num

    print('#{} {}'.format(tc, max_house))