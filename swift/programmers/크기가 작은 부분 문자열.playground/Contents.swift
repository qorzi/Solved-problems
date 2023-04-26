import Foundation

func solution(_ t:String, _ p:String) -> Int {
    let cnt = t.count - p.count
    var substr: [Int] = []
    for i in 0...cnt {
        let startIdx = t.index(t.startIndex, offsetBy: i)
        let endIdx = t.index(t.startIndex, offsetBy: i + p.count)
        if endIdx <= t.endIndex, let sub = Int(t[startIdx..<endIdx]) {
            substr.append(sub)
        }
    }

    var result = 0
    for el in substr {
        if let num = Int(p), el <= num {
            result += 1
        }
    }
    
    return result
}
