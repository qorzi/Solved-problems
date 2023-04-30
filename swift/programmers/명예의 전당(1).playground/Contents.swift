import Foundation

func solution(_ k:Int, _ score:[Int]) -> [Int] {
    var best:[Int] = []
    var result:[Int] = []
    for (i, el) in score.enumerated() {
          best.append(el)
          best.sort()
          if i >= k {
               best.removeFirst()
          }

          result.append(best[0])
     }

     return result
}
