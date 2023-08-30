#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Edge
{
    int v, w;
};

int N, M;
vector<char> gender;
vector<vector<Edge>> adj;
vector<bool> visited;

int prim()
{
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, 1});
    int totalWeight = 0;
    int cnt = 0;

    while (!pq.empty())
    {
        int w = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (visited[u])
            continue;
        visited[u] = true;
        totalWeight += w;
        cnt++;

        for (const auto &edge : adj[u])
        {
            if (!visited[edge.v] && gender[u] != gender[edge.v])
            {
                pq.push({edge.w, edge.v});
            }
        }
    }

    if (cnt == N)
        return totalWeight;
    return -1;
}

int main()
{
    cin >> N >> M;
    gender.resize(N + 1);
    adj.resize(N + 1);
    visited.resize(N + 1, false);

    for (int i = 1; i <= N; i++)
    {
        cin >> gender[i];
    }

    for (int i = 0; i < M; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    cout << prim() << endl;

    return 0;
}
