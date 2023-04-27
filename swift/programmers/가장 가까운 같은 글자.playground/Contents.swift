import Foundation

// s = "banana"
func solution(_ s:String) -> [Int] {
    var exIndex: [Character: Int] = [:]
    var result = s.enumerated().map{ (i, str) -> Int in
        if let exindex = exIndex[str] {
            var v = i - exindex
            exIndex[str] = i
            return v
        } else {
            exIndex[str] = i
            return -1
        }
    }
    return result
}
