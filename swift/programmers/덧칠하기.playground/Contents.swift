import Foundation

func solution(_ n:Int, _ m:Int, _ section:[Int]) -> Int {
    var cnt = 0
    var max = 0
    section.forEach{ el in
        if max < el {
            max = el + m - 1
            cnt += 1
        }
    }
    return cnt
}
