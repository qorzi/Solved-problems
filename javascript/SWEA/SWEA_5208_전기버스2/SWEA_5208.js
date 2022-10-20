// T = int(input())
// for tc in range(1, T+1):
//     lst = list(map(int, input().split()))
//     N = lst.pop(0)

//     go_cnt = 0
//     change_cnt = -1
//     bettery = 1
//     keep = 0
//     keep_cnt = 0
//     while lst:
//         go_cnt += 1
//         bettery -= 1
//         new_bettery = lst.pop(0)
//         keep_cnt += 1

//         # 남은 배터리가 이동 할 정거장 수보다 크다면, 이동
//         if N - go_cnt <= bettery:
//             continue

//         if keep - keep_cnt < N - go_cnt:
//             if keep - keep_cnt < new_bettery:
//                 keep = new_bettery
//                 keep_cnt = 0

//         if bettery == 0:
//             bettery = keep - keep_cnt
//             change_cnt += 1

//     print('#{} {}'.format(tc, change_cnt))

