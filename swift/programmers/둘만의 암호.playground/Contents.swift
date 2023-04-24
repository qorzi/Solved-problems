import Foundation

func solution(_ s: String, _ skip: String, _ index: Int) -> String {
    let alpha = Array("abcdefghijklmnopqrstuvwxyz")
    let oldStr = Array(s)
    let skipStr = Set(skip)
    let hashMap = Dictionary(uniqueKeysWithValues: alpha.enumerated().map { ($1, $0) })

    var resultLst = oldStr.map { str -> Character in
        if let newIndex = hashMap[str] {
            var cnt = 0
            var actualIndex = newIndex

            while cnt < index {
                actualIndex = (actualIndex + 1) % alpha.count
                if !skipStr.contains(alpha[actualIndex]) {
                    cnt += 1
                }
            }

            return alpha[actualIndex]
        }
        return str
    }

    let result = String(resultLst) // [Character] -> String

    return result
}
