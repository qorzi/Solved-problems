import Foundation

func solution(_ park:[String], _ routes:[String]) -> [Int] {
    let direction : [String:(Int,Int)] = ["E":(0,1), "W":(0,-1), "S":(1,0), "N":(-1,0)]
    
    // 이차원 배열 설정
    var map: [[Int]] = []
    var start: (Int, Int) = (0, 0)
    for (i, str) in park.enumerated() {
        var row: [Int] = []
        for (j, char) in str.enumerated() {
            if char == "O" {
                row.append(0) // 0 빈공간
            } else if char == "X" {
                row.append(1) // 1 장애물
            } else {
                row.append(2) // 2 시작 위치
                start = (i, j)
            }
        }
        map.append(row)
    }
    
    // route 설정
    let newRoutes = routes.map { $0.components(separatedBy: " ") }
    for el in newRoutes {
        if let dir = direction[el[0]], let cnt = Int(el[1]) {
            start = move(start, dir, cnt, map)
        }
    }
    return [start.0, start.1]
}

func move(_ start:(Int, Int), _ direction:(Int, Int), _ cnt:Int, _ map:[[Int]]) -> (Int, Int) {
    var (current_i, current_j) = start
    let (save_i, save_j) = start
    let (di, dj) = direction
    let row = map.count
    let col = map[0].count
    var isPossible = true
    
    for _ in 1...cnt {
        if 0..<row ~= current_i + di && 0..<col ~= current_j + dj {
            if map[current_i + di][current_j + dj] != 1 {
                current_i += di
                current_j += dj
            } else {
                isPossible = false
                break
            }
        } else {
            isPossible = false
            break
        }
    }
    
    return isPossible ? (current_i, current_j) : (save_i, save_j)
    
}
