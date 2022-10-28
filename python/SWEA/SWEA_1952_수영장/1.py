import sys
sys.stdin = open('sample_input.txt', 'r')

# 현재 달부터 3개월 치 계산
def month3_price(month, total):
    global ans

    if month >= 12:
        if total < ans:
            ans = total
        return

    month3_price(month+1, total+month_prices[month])
    month3_price(month+3, total+month_3)

# 전체 이용 횟수를 이용해서 최소 비용으로 이용권을 구매
T = int(input())
for tc in range(1, T+1):
    day, month_1, month_3, year = map(int, input().split()) # 1일 1달 3달 1년 이용권 가격
    use_day_for_month = list(map(int, input().split())) # 달마다 이용 횟수

    month_prices = []
    # 월 별 이용권 가격 판단
    for using_day in use_day_for_month:
        if using_day >= month_1//day:
            month_prices.append(month_1)
        else:
            month_prices.append(using_day*day)

    # 3개월 단위 판단
    ans = 99999999
    month3_price(0, 0)

    if year < ans: # 1 년치 이용권이 더 싸다면,
        ans = year

    print('#{} {}'.format(tc, ans))