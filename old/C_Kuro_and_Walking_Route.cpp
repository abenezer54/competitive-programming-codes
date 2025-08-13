#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, x, y; cin >> n >> x >> y;
    --x; --y;
    vector<vector<int>> adj(n);
    
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        --u; --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> vis(n);

    function<void(int)> dfs = [&] (int node) {
        for (auto nei: adj[node]) {
            if (vis[nei] == 0) {
                vis[nei] = 1;
                dfs(nei);
            }
        }

    };
   
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t = 1;
    // cin >> t;
    
    while (t--) {
        solve();
    }
    
    return 0;
}