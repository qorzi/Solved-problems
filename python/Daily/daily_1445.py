def leap_year(N):
    if not N % 4 and N % 100 or not N % 400:
        return f'{N}년은 윤년입니다.'
    else:
        return f'{N}년은 윤년이 아닙니다.'

print(leap_year(2021))
print(leap_year(2020))