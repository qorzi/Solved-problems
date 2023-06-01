T = int(input())
nums = list(int(input()) for _ in range(T))

for num in nums:
    seperate = [str(n) for n in str(num)]

    # 리스트의 뒤에서부터 앞으로 탐색하면서, i-1번째 원소가 i번째 원소보다 작은 경우를 찾음
    i = len(seperate) - 1
    while i > 0 and seperate[i-1] >= seperate[i]:
        i -= 1

    # 만약 주어진 숫자가 이미 최대라면, "BIGGEST"을 반환
    if i <= 0:
        print("BIGGEST")
        continue

    # i-1번째 원소보다 큰 가장 작은 원소를 찾아서 i-1번째 원소와 교환, i부터는 내림차순 정렬이라 큰걸 찾자마자 바꾸면 됨
    j = len(seperate) - 1
    while seperate[j] <= seperate[i-1]:
        j -= 1
    seperate[i-1], seperate[j] = seperate[j], seperate[i-1]

    # i부터 오른차순 정렬을 해주면 다음으로 큰 수가 된다.
    new_left = seperate[:i]
    new_right = seperate[i:]
    new_right.sort()

    new = new_left + new_right

    next_bigger = int(''.join(new))
    print(next_bigger)
