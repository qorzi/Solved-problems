#include <bits/stdc++.h>
using namespace std;

int a;
int main() {
    cout << &a << endl;
    a = 0;
    cout << &a << endl;

    int *b = &a;
    cout << b << endl;
    cout << sizeof(b) << endl;
    cout << *b << endl;

    *b = 7;
    cout << a << endl;

}