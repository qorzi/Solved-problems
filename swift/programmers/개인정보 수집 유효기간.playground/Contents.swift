import Foundation

// 풀이 : 단위마다 비교하지 말고 가장 처음, 하나의 단위로 변경가능한지부터 생각하자!

func solution(_ today:String, _ terms:[String], _ privacies:[String]) -> [Int] {
    let newDay = today.split(separator: ".").map { Int($0)! }
    let newTerms = Dictionary(uniqueKeysWithValues: terms.map{ ($0.split(separator: " ")[0], Int($0.split(separator: " ")[1])!) })
    let newPri = privacies.map{ $0.split(separator: " ") }.map{ ($0[0].split(separator: ".").map { Int($0)! }, $0[1]) }

    
    let toDay = newDay[0]*12*28 + newDay[1]*28 + newDay[2]

    var result: [Int] = []
    for (i, el) in newPri.enumerated() {
        if let term = newTerms[el.1] {
            let ex = el.0[0]*12*28 + el.0[1]*28 + el.0[2] + term*28
            if ex <= toDay {
                result.append(i+1)
            }
        }
    }
    return result
}
