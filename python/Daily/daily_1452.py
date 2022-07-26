def mass_percent():
    #인자 받기
    B_per = []
    B_g = []
    for _ in range(5):
        #str로 최대 5번까지 인자를 받는다.

        N = input('소금물의 농도(%)와 소금물의 양(g)을 입력하십시오:')
        # print(N)

        #N에 Done이 입력된다면, 받는걸 멈춘다.
        if N == 'Done':
            # print('Done')
            break
        else:
            x = N[:N.find('%')]
            y = N[N.find(' ')+1:N.find('g')]

            B_per += [int(x)]
            B_g += [int(y)]
    
    #소금의양
    C_list = []
    for i in range(len(B_per)):
        C_list += [(B_per[i]*B_g[i])/100]
    
    C_salt = sum(C_list)
    
    #전체 소금물의 g
    D = 0
    for i in range(len(B_per)):
        D += B_g[i]
    
    #최종 농도
    F = int(C_salt)/int(D)*100

    return f'{round(F, 2)}% {round(D, 2)}g'

    

print(mass_percent())