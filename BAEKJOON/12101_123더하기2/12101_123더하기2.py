def ans(n, k, cur, lst=[]):
    now = sum(lst)

    if now == n:
        cur[0] += 1
        if cur[0] == k:
            return lst[:]
    elif now > n:
        return
    
    for i in range(1, 4):
        lst.append(i)
        res = ans(n, k, cur, lst)
        if res: 
            return res
        lst.pop()

N, K = map(int, input().split())  # 목표 숫자, 사전 순서
res = ans(N, K, [0], [])
if res:
    print('+'.join(map(str, res)))
else:
    print(-1)
