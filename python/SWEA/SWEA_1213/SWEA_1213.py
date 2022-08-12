import sys
sys.stdin = open('input_1213.txt', 'rt', encoding='UTF8')

for tc in range(1, 11):
    tc_trash = int(input())
    str_1 = input()
    str_2 = input()

    num = len(str_2) - len(str_1) + 1

    #문자1과 같은 길이로 문자2를 잘라서 확인
    str_num = 0
    for i in range(num):
        #슬라이싱 한것이 str_1과 같은지 확인
        if str_1 == str_2[i:i+len(str_1)]:
            str_num += 1

    print(f'#{tc} {str_num}')