cards = [1, 1, 2, 2, 3, 3]

triplet = False
double_tr = False
run = False
double_run = False
baby_gin = False

#triplet 판별
#doubl_case 판별
for _ in range(2):
    #cards를 두번 돌려서 요소가 몇번 겹치는지 판별한다.
    for i in cards:
        same_count = 0
        for j in cards:
            if j == i:
                same_count += 1

        #겹치는 횟수 판별 후, 3회 이상이라면 트리플렛으로 확정짓고 요소 제거한다.
        if same_count >= 3:
            cards.remove(i)
            cards.remove(i)
            cards.remove(i)
            if triplet == False:
                triplet = True
            elif triplet == True:
                double_tr = True

    #남은 숫자를 오름차순 정렬하고 연이은 숫자인지 판별한다.
    #오름차순 정렬
    for i in range(len(cards)-1, 0, -1):
        for j in range(0, i):
            if cards[j] > cards[j+1]:
                cards[j], cards[j+1] = cards[j+1], cards[j]

    #연이은 숫자인지 판별한다.
    plus_count = 0
    for i in cards:
        if (i+1) in cards and (i+2) in cards:
            cards.remove(i)
            cards.remove(i+1)
            cards.remove(i+2)

            if run == False:
                run = True
            elif run == True:
                double_run = True

if (triplet and run) or double_run or double_tr:
    baby_gin = True

print(triplet, run, double_tr, double_run)
print(baby_gin)