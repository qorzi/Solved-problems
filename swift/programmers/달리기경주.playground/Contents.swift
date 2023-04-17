import Foundation

let players = ["mumu", "soe", "poe", "kai", "mine"]
let callings = ["kai", "kai", "mine", "mine"]

// 시간초과
func solution(_ players:[String], _ callings:[String]) -> [String] {
    var newPlayers = players
    for name in callings {
        if let index = newPlayers.firstIndex(of: name), index > 0 {
            newPlayers.swapAt(index, index - 1)
        }
    }
    return newPlayers
}

// ---

// key-value 형태로 이름과 인덱스를 해쉬맵으로 만들고 진행한다.
func solution2(_ players:[String], _ callings:[String]) -> [String] {
    var newPlayers = players
    var playerIndices: [String: Int] = [:]

    // hash map - 인덱스 해쉬화
    for (index, name) in newPlayers.enumerated() {
        playerIndices[name] = index
    }

    for name in callings {
        if let currentIndex = playerIndices[name], currentIndex > 0 {
            let newIndex = currentIndex - 1
            // 인덱스 앞으로 한칸
            newPlayers.swapAt(currentIndex, newIndex)
            // 해쉬맵 업데이트
            playerIndices[name] = newIndex
            playerIndices[newPlayers[currentIndex]] = currentIndex
        }
    }
    return newPlayers
}

// ---

// 해쉬맵 간략화
func solution3(_ players:[String], _ callings:[String]) -> [String] {
    var newPlayers = players
    var playerIndices = Dictionary(uniqueKeysWithValues: players.enumerated().map { ($1, $0) })

    for name in callings {
        if let currentIndex = playerIndices[name], currentIndex > 0 {
            let newIndex = currentIndex - 1
            newPlayers.swapAt(currentIndex, newIndex)
            playerIndices[name] = newIndex
            playerIndices[newPlayers[currentIndex]] = currentIndex
        }
    }
    return newPlayers
}

