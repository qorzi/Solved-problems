N = int(input())

nums = [int(input()) for _ in range(N)]
max_num = max(nums)

dp = [0, 1, 2, 4]

for i in range(4, max_num+1):
    next = dp[i-1] + dp[i-2] + dp[i-3]
    next %= 1000000009
    dp.append(next)

for i in nums:
    print(dp[i])