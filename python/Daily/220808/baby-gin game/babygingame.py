cards = [1, 3, 2, 1, 1, 1]

triplet = False
run = False
baby_gin = False

#triplet 판별
#cards를 두벌 돌려서 요소가 몇번 겹치는지 판별한다.
for i in cards:
    same_count = 0
    for j in cards:
        if j == i:
            same_count += 1

    #겹치는 횟수 판별 후, 3회 이상이라면 트리플렛으로 확정짓고 요소 제거한다.
    if same_count >= 3:
        triplet = True
        cards.remove(i)
        cards.remove(i)
        cards.remove(i)
        break

#남은 숫자를 오름차순 정렬하고 연이은 숫자인지 판별한다.
#오름차순 정렬
for i in range(len(cards)-1, 0, -1):
    for j in range(0, i):
        if cards[j] > cards[j+1]:
            cards[j], cards[j+1] = cards[j+1], cards[j]

#연이은 숫자인지 판별한다.
plus_count = 0
for i in range(len(cards)-1):
    if cards[i+1] == cards[i]+1:
        plus_count += 1
    if plus_count >= 2:
        run = True
        break

if triplet and run:
    baby_gin = True

print(baby_gin)