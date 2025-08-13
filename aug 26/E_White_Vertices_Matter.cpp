// author: Nardos Wehabe

#include "bits/stdc++.h"

using namespace std;
typedef long long ll;
// typedef __int128 lll;

void solve()
{
    int N;
    cin >> N;
    vector<int> color(N);
    for (auto &ai : color)
    {
        cin >> ai;
        if (!ai)
            ai = -1;
    }

    vector<int> adj[N];
    for (int i = 0; i < N - 1; ++i)
    {
        int u, v;
        cin >> u >> v;
        u--, v--;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }


}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int tt = 1;
    // cin >> tt;

    while (tt--)
        solve();
}
