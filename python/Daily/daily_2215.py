N = int(input())

if not N % 4 and N % 100 or not N % 400:
    print('윤년이다.')
else:
    print('윤년이 아니다')
