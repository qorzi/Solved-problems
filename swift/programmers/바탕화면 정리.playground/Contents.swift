import Foundation

func solution(_ wallpaper:[String]) -> [Int] {
    var stack_i : [Int] = []
    var stack_j : [Int] = []
    for (i, row) in wallpaper.enumerated() {
        for (j, col) in row.enumerated() {
            if col == "#" {
                stack_i.append(i)
                stack_j.append(j)
            }
        }
    }
    let result = [stack_i.min()!, stack_j.min()!, stack_i.max()! + 1, stack_j.max()! + 1]
    return result
}
