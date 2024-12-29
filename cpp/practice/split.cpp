#include <bits/stdc++.h>
using namespace std;

vector<string> split(const string &input, string delimiter) {
  vector<string> result;
  auto start = 0;
  auto end = input.find(delimiter, start); // 수정: start부터 검색
  while (end != string::npos) {
    result.push_back(input.substr(start, end - start)); // 분리된 부분 추가
    start = end + delimiter.size();     // 다음 검색 시작 위치로 이동
    end = input.find(delimiter, start); // 수정: start 이후부터 검색
  }
  result.push_back(input.substr(start)); // 마지막 부분 추가
  return result;
}

int main() {
  string a = "apple, banana, orange, graph";
  vector<string> res = split(a, " ");
  for (auto r : res)
    cout << r << " ";
  return 0;
}