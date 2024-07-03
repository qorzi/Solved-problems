def count(n):
    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    if n >= 4:
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]


N = int(input())
numbers = [int(input()) for _ in range(N)]
for n in numbers:
    print(count(n))