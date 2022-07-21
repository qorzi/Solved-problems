input_list = [1,1,3,3,0,1,1]

output_list = []
var_before = -1

#for문을 이용해 input_list의 요소를 하나씩 가져온다.
for i in input_list:
    #가져온 요소를 output_list에 넣는다.
    output_list += [i]
    #만약, 넣은 요소가 이전 값과 같다면 pop으로 뺀다.
    if var_before == i:
        output_list.pop()
    #다 이용한 이전 요소는 새롭게 i로 변경한다.
    var_before = i

print(output_list)