n, k = map(int, input().split())    # 물건의 수, 버틸수 있는 무게
items = [tuple(map(int, input().split())) for _ in range(n)]    # 물건의 무게, 물건의 가치

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        ex_w, ex_v = items[i-2]
        w, v = items[i-1]
        if w <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][(j-w)] + v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])