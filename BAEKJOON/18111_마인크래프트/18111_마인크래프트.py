N, M, B = map(int, input().split())  # 시간 복잡도 O(1)
flat_ground = [int(i) for _ in range(N) for i in input().split()]


def best_ground_height():
    min_time = 500*500*2*256
    best_height = 0
    min_height = min(flat_ground)
    max_height = max(flat_ground)

    for height in range(min_height, max_height + 1):
        if available(height):
            time = count_time(height)
            if time <= min_time:
                min_time = time
                if height >= best_height:  # 최대 높이를 구해야함.
                    best_height = height

    return min_time, best_height


def available(height):
    ground_cnt = len(flat_ground)
    all_available_block = sum(flat_ground) + B
    target_block = ground_cnt * height

    return all_available_block >= target_block


def count_time(height):
    time = 0

    for el in flat_ground:
        if el > height:
            time += (el - height) * 2
        elif height > el:
            time += (height - el)

    return time


min_time, best_height = best_ground_height()

print(min_time, best_height)
