#include <bits/stdc++.h>
#include <iostream>

using namespace std;

int main() {
    vector<int> v{1, 1, 2, 2, 3, 3, 4, 2, 5, 6, 2, 6};
    // auto it = unique(v.begin(), v.end()); // 중복 제거

    // 유효 범위 출력
    // for (auto i = v.begin(); i != it; ++i)
    //   cout << *i << " ";
    // cout << '\n';

    sort(v.begin(), v.end()); // unique는 연속된 중복만 제거하기 때문에 sort필요
    v.erase(unique(v.begin(), v.end()), v.end()); // 중복 제거

    for (int i : v) {
        cout << i << " ";
    }
    cout << endl;

    vector<int> vv = {3, 1, 2, 1, 3, 2};
    // set 방식이 메모리 사용량은 더 큼
    set<int> s(vv.begin(), vv.end()); // 중복 제거 및 정렬
    for (int i : s) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
} 