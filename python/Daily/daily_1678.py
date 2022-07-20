orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

#단일 str 구분해서 리스트로 받기
order_list = list(orders.split(','))
print(len(order_list))

#중복 제거
order_list = set(order_list)
order_list = list(order_list)

#내림차순 정렬
order_list.sort()
order_list.reverse()

print(order_list)