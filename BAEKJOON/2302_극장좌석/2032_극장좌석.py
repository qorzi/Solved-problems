def seating(N, VIP):
    dp = [0 for _ in range(N+1)]
    dp[0], dp[1] = 1, 1
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    VIP.insert(0, 0)
    VIP.append(N+1)

    answer = 1
    for i in range(1, len(VIP)):
        answer *= dp[VIP[i] - VIP[i-1] - 1]
    return answer


N = int(input())
M = int(input())
VIP = [int(input()) for _ in range(M)]
print(seating(N, VIP))
