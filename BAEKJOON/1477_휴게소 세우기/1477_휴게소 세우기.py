# 현재 휴게소의 개수 N, 더 지으려고 하는 휴게소의 개수 M, 고속도로의 길이 L
N, M, L = map(int, input().split())

# 현재 휴게소의 위치
rest_areas = list(map(int, input().split()))
rest_areas.append(0)  # 출발점 추가
rest_areas.append(L)  # 도착점 추가
rest_areas.sort()  # 일단 정렬

start = 1  # 가능한 최소 거리
end = L  # 가능한 최대 거리

while start <= end:
    mid = (start + end) // 2  # 가운데 거리
    count = 0  # 추가로 설치해야 하는 휴게소의 수

    # 휴게소 간의 거리가 mid보다 클 경우, 휴게소를 추가로 설치해야 함
    for i in range(1, N + 2):
        if rest_areas[i] - rest_areas[i - 1] > mid:
            count += (rest_areas[i] - rest_areas[i - 1] - 1) // mid

    # 추가로 설치해야 하는 휴게소의 수가 M보다 작거나 같다면, mid를 감소시킴
    if count <= M:
        end = mid - 1
    # 그렇지 않다면, mid를 증가시킴
    else:
        start = mid + 1

print(start)
