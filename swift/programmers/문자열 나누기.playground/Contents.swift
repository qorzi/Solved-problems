import Foundation

func solution(_ s:String) -> Int {
    var result = 0
    var x: Character? = nil
    var xCount = 0

    for chr in s {
        if x == nil {
            x = chr
            xCount = 1
            result += 1
            continue
        }

        xCount += x == chr ? 1 : -1

        if xCount == 0 {
            x = nil
        }
    }

    return result
}
