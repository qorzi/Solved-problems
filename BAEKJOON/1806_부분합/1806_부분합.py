N, S = map(int, input().split())
numbers = list(map(int, input().split()))

if sum(numbers) < S:
    print(0)
else:
    min_length = N + 1
    current_sum = 0
    start = 0

    for end in range(N):
        current_sum += numbers[end]

        while current_sum >= S:
            min_length = min(min_length, end - start + 1)
            current_sum -= numbers[start]
            start += 1
    print(min_length)