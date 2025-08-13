#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, m, k; cin >> n >> m >> k;
    vector<int> c(n + 1);
    vector<vector<int>> adj(n + 1);
    for (int i = 1; i <=n; i++) {
        cin >> c[i];
    }
    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        adj[v].push_back(u);
        adj[u].push_back(v);
    }

    vector<int> vis(n + 1);
    map<int, int> col;
    int cur_max = 0;

    function<int(int)> dfs = [&] (int node) {
        vis[node] = 1;
        int sz = 1;
        col[c[node]]++;
        for (auto nei: adj[node]) {
            if (vis[nei] == 0) {
                sz += dfs(nei);
            } 
        }
        return sz;
    };

    int ans = 0;
    for (int node = 1; node <= n; node++) {
        if (vis[node] == 0) {
            col.clear();
            int sz = dfs(node);
            cur_max = 0;
            for (auto [key, val]: col) {
                cur_max = max(cur_max, val);
            }
            ans += sz - cur_max;
        }
    }
   
    cout << ans << endl;
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