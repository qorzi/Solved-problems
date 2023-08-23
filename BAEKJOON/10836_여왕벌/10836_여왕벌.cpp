#include <bits/stdc++.h>
using namespace std;

int M, N;
vector<vector<int>> grid;

void grow(int zcnt, int ocnt, int tcnt)
{
    vector<vector<int>> tmp = grid;

    for (int i = 0; i < M; i++)
    {
        if (zcnt > 0)
        {
            tmp[M - i - 1][0] += 0;
            zcnt--;
        }
        else if (ocnt > 0)
        {
            tmp[M - i - 1][0] += 1;
            ocnt--;
        }
        else
        {
            tmp[M - i - 1][0] += 2;
            tcnt--;
        }
    }

    for (int j = 1; j < M; j++)
    {
        if (zcnt > 0)
        {
            tmp[0][j] += 0;
            zcnt--;
        }
        else if (ocnt > 0)
        {
            tmp[0][j] += 1;
            ocnt--;
        }
        else
        {
            tmp[0][j] += 2;
            tcnt--;
        }
    }

    for (int i = 1; i < M; i++)
    {
        for (int j = 1; j < M; j++)
        {
            int grow_max = max({(tmp[i - 1][j] - grid[i - 1][j]), (tmp[i][j - 1] - grid[i][j - 1]), (tmp[i - 1][j - 1] - grid[i - 1][j - 1])});
            tmp[i][j] += grow_max;
        }
    }

    grid = tmp;
}

int main()
{
    ios_base::sync_with_stdio(false); // 버퍼동기화 끄기
    cin.tie(NULL);                    // cout 방출 해제

    cin >> M >> N;
    grid = vector<vector<int>>(M, vector<int>(M, 1));

    for (int i = 0; i < N; i++)
    {
        int zcnt, ocnt, tcnt;
        cin >> zcnt >> ocnt >> tcnt;
        grow(zcnt, ocnt, tcnt);
    }

    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cout << grid[i][j] << ' ';
        }
        cout << '\n';
    }

    return 0;
}