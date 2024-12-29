#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> arr(N+1, 0);
    vector<int> psum(N+1, 0);

    // 입력 배열
    for (int i = 1; i <= N; i++) {
        cin >> arr[i];
        psum[i] = psum[i-1] + arr[i]; // 누적합
    }
    
    // 결과 처리
    for (int i = 0; i < M; i++) {
        int A, B;
        cin >> A >> B;
        cout << psum[B] - psum[A-1] << "\n";
    }
    return 0;
}