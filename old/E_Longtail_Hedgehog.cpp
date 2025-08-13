#include <bits/stdc++.h>
using namespace std;

using vi = vector<int>;
using vvi = vector<vi>;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    vvi adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vi vis(n + 1, 0);
    int ans = 0;

    for (int start = 1; start <= n; ++start) {
        if (vis[start] == 0) {
            stack<pair<int, int>> stk;
            stk.push({start, 1});
            while (!stk.empty()) {
                auto [node, length] = stk.top();
                stk.pop();
                vis[node] = length;
                ans = max(ans, length * (int)adj[node].size());
                for (int nei : adj[node]) {
                    if (nei > node && vis[nei] < length + 1) {
                        stk.push({nei, length + 1});
                    }
                }
            }
        }
    }

    cout << ans << "\n";

    return 0;
}
