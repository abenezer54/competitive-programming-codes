#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, m; cin >> n >> m;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    vector<vector<int>> adj(n);
    
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        --u; --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> vis(n);

    function<int(int, int)> dfs = [&] (int node, int cnt) {
        if (a[node]) cnt += a[node];
        else cnt = 0;

        int tot = 0;
        if (adj[node].size() == 1 && node != 0) return 1;
        

        for (auto nei: adj[node]) {
            if (vis[nei] == 0 && cnt + a[nei] <= m) {
                vis[nei] = 1;
                tot += dfs(nei, cnt);
            }
        }

        return tot;
    };

    vis[0] = 1;
    cout << dfs(0, 0) << endl;
   
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