# 회전 초밥 벨트에 놓인 접시의 수 n, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
n, d, k, c = map(int, input().split())

# 회전 초밥
rotate_sushi = [int(input()) for _ in range(n)]

# 모든 종류 스시
all_sushi_set = set(rotate_sushi + [c])  # c 스시가 없는 정신나간 경우가 있다?!

# 모든 스시 카운트
sushi_count_dict = {sushi: 0 for sushi in all_sushi_set}

# 원형 스시
rotate_sushi += rotate_sushi[:k]

# 초기 윈도우에 대한 스시 개수 세기
count = 0
for i in range(k):
    sushi_count_dict[rotate_sushi[i]] += 1
    if sushi_count_dict[rotate_sushi[i]] == 1:
        count += 1

best_sushi = count

# 슬라이딩 윈도우를 이용한 리스트 갱신
for i in range(k, n+k):

    sushi_count_dict[rotate_sushi[i]] += 1  # 새롭게 추가되는 초밥을 dict에 추가
    if sushi_count_dict[rotate_sushi[i]] == 1:
        count += 1

    sushi_count_dict[rotate_sushi[i-k]] -= 1  # 윈도우에서 빠지는 초밥을 dict에서 제거
    if sushi_count_dict[rotate_sushi[i-k]] == 0:
        count -= 1

    # c 유무에 따라 카운트 +1
    if sushi_count_dict[c] == 0:
        crr_sushi = count + 1
    else:
        crr_sushi = count

    # 현재 초밥 종류의 수가 최대이면 업데이트
    if crr_sushi >= best_sushi:
        best_sushi = crr_sushi

print(best_sushi)
