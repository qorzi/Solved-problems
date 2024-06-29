N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

cnt = 0
for i in range(N):
    target = numbers[i]
    l = 0
    r = N - 1

    while l < r:
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue

        current_sum = numbers[l] + numbers[r]
        if current_sum == target:
            cnt += 1
            break
        elif current_sum < target:
            l += 1
        else:
            r -= 1
print(cnt)