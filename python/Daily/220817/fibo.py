#일반적 재귀
def fibo1(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

#메모이제이션
def fibo2(n):
    if memo[n] == -1:
        memo[n] = fibo(n-1) + fobo(n-2)
    return memo[n]

#memo 리스트 크기랑 최소로 시작할 값은 넣어두자
memo = [-1]*101
memo[0] = 0
memo[1] = 1

#동적계획 DP
def fibo3(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])

    return f[n]


for i in range(20):
    print(i, fibo(i))