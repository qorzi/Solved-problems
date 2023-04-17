import Foundation

func solution(_ name:[String], _ yearning:[Int], _ photo:[[String]]) -> [Int] {
    var points : [Int] = []
    // 해쉬맵
    var hashMap : [String : Int] = [:]
    
    for (i, name) in name.enumerated() {
        hashMap[name] = yearning[i]
    }
    
    // 점수 계산
    for mans in photo {
        var value = 0
        for name in mans {
            if let point = hashMap[name] {
                value += point
            }
        }
        points.append(value)
    }
    return points
}

// ---
// 다른 사람 풀이
func solution2(_ name:[String], _ yearning:[Int], _ photo:[[String]]) -> [Int] {
    let score: [String: Int] = Dictionary(uniqueKeysWithValues: zip(name, yearning))
    return photo.map { $0.reduce(0) { $0 + (score[$1] ?? 0) } }
}
