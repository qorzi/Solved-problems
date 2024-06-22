
def is_contain(M, size, lst): # 현재 사이즈로 강의가 전부 담기는지 여부 반환
    cnt = 1
    current_blue = 0
    for el in lst:
        if current_blue + el > size:
            cnt += 1
            current_blue = el
            if cnt > M:
                return False
        else:
            current_blue += el
    return True

def get_bluelay_size(M, lst): # 모든 강의를 나눠 담을수 있는 최소한 크기 반환
    # 범위 설정
    # 각 블루레이는 가장 큰 강의 보다 용량이 커야한다.
    min_size = max(lst)
    # 최대 값은 모든 강의를 하나의 블루레이에 담는 경우이다.
    max_size = sum(lst)

    while min_size < max_size:
        mid_size = (min_size+max_size)//2
        if is_contain(M, mid_size, lst):
            max_size = mid_size
        else:
            min_size = mid_size+1

    return min_size


N, M = map(int, input().split()) # 강의의 수, 블루레이의 수
lectures_min = list(map(int, input().split())) # 각 강의 시간

print(get_bluelay_size(M, lectures_min))