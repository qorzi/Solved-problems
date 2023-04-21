import Foundation

func solution(_ cards1: [String], _ cards2: [String], _ goal: [String]) -> String {
    // reversed로 뒤집은 배열을 Array로 감싸 다시 기존 배열 타입으로 바꿔줘야한다.
    var newCards1 = Array(cards1.reversed())
    var newCards2 = Array(cards2.reversed())

    var result = "Yes"
    goal.forEach { el in
        if el == newCards1.last {
            newCards1.removeLast()
        } else if el == newCards2.last {
            newCards2.removeLast()
        } else {
            result = "No"
        }
    }

    return result
}
