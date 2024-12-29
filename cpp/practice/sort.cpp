#include <iostream>
#include <vector>
#include <algorithm> // sort 포함
using namespace std;

int main() {
    vector<int> v = {5, 3, 8, 1, 2};

    sort(v.begin(), v.end()); // 기본: 오름차순

    for (int i : v) {
        cout << i << " ";
    }
    cout << endl;

    sort(v.begin(), v.end(), greater<int>()); // 내림차순

    for (int i : v ) {
        cout << i << " ";
    }
    cout << endl;

    sort(v.begin(), v.end(), [](int a, int b) {
        return (a % 2 == 0 && b % 2 != 0) || (a % 2 == b % 2 && a < b); // 짝수 우선선
    });

    for (auto i : v) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
