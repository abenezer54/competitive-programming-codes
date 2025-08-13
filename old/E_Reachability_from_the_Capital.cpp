#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, m, s; cin >> n >> m >> s;
    vector<vector<int>> adj(n + 1);
    vector<int> ind(n + 1);

    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        ind[v]++;
    }

    vector<int> col(n + 1), col2(n + 1);
    set<int> cycles;

    function<void(int)> dfs = [&] (int node) {
        col[node] = 1;
        for (int nei: adj[node]) {
            if (col[nei] == 0) {
                dfs(nei);
            }  
        }
    };

    function<void(int)> dfs_for_cycle = [&] (int node) {
        col2[node] = 1;
        for (int nei: adj[node]) {
            if (col2[nei] == 0) {
                dfs_for_cycle(nei);
            } else if (col2[nei] == 1) {
                cycles.insert(nei);
            }
        }
        col2[node] = 2;
    };


    dfs(s);
    int ans = 0; 
    for (int node = 1; node <= n; node++) {
        if (col[node] == 0  && ind[node] == 0) {
            ans++;
            dfs(node);
        }
    }
    
    for (int node = 1; node <= n; node++) {
        if (col2[node] == 0) {
            dfs_for_cycle(node);
        }
    }

    for (auto start: cycles) {
        if (col[start] == 0) {
            dfs(start);
            ans++;
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