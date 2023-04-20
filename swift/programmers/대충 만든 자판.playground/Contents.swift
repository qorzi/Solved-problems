import Foundation

func solution(_ keymap:[String], _ targets:[String]) -> [Int] {
    var dicMap : [String : Int] = [:]
    
    // 각 문자열마다 최소 인덱스를 딕셔너리에 저장
    for el in keymap {
        for (i, str) in el.enumerated() {
            let strString = String(str)
            if let key = dicMap[strString] {
                if i+1 < key {
                    dicMap[strString] = i+1
                }
            } else {
                dicMap[strString] = i+1
            }
        }
    }
    
    var result : [Int] = []
    // 각 문자열의 각 문자가 딕셔너리에 저장된 값을 더함
    for el in targets {
        var cnt = 0
        for str in el {
            if let value = dicMap[String(str)] {
                cnt += value
            } else {
                cnt = -1
                break
            }
        }
        result.append(cnt)
    }
    return result
}
