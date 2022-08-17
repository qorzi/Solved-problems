num_dice = int(input())
dice_list = [list(map(int, input().split())) for _ in range(num_dice)]

#주사위 위-아래 정리
dice_dict = []
for i in dice_list:
    dice_dict += [{i[0]: i[5], i[1]: i[3], i[2]: i[4], i[3]: i[1], i[4]: i[2], i[5]: i[0]}]



dice = [1, 2, 3, 4, 5, 6]

dice_side_max_list = []
#주사위는 6개의 요소를 가짐
for j in range(1,7):
    # j가 바닥 일 때, 
    bottom = j
    top = dice_dict[0][j]
    dice_side_max_elements_sum = 0
    #주사위의 갯수만큼
    for i in range(num_dice):
        dice_side_elements = list(set(dice) - {bottom, top,})
        dice_side_max_elements_sum += max(dice_side_elements)
        bottom = top
        try:
            top = dice_dict[i+1][bottom]
        except:
            pass
    dice_side_max_list += [dice_side_max_elements_sum]

print(max(dice_side_max_list))
    
    

