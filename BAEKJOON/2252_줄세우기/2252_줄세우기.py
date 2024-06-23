def make_student_list(N, lst):
    total_student = [0 for _ in range(N+1)] # 전체 학생 체크 리스트
    line = []

    for s1, s2 in lst:
        if total_student[s1] == 0 and total_student[s2] == 0:
            total_student[s1], total_student[s2] = 1, 1
            line.append(s1)
            line.append(s2)
        elif total_student[s1] == 1 and total_student[s2] == 0:
            total_student[s2] = 1
            line.append(s2)
        elif total_student[s1] == 0 and total_student[s2] == 1:
            total_student[s1] = 1
            s2_pos = line.index(s2)
            line.insert(s2_pos, s1)
        else:
            s1_pos = line.index(s1)
            s2_pos = line.index(s2)
            if s1_pos > s2_pos:
                line.remove(s1)
                s2_pos = line.index(s2)
                line.insert(s2_pos, s1)

    for i in range(1, N+1):
        if total_student[i] == 0:
            total_student[i] = 1
            line.append(i)
    
    return line

N, M = map(int, input().split()) # 학생 수, 비교 수
compairisom_lst = [map(int, input().split()) for _ in range(M)] # 학생 키 비교 리스트

print(*make_student_list(N, compairisom_lst))
