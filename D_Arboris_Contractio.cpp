#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n; cin >> n;
    vector<int> ind(n + 1), deg(n + 1), val(n + 1), vis(n + 1);
    
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        ind[u]++; deg[v]++; 
        ind[v]++; deg[u]++;
        adj[v].push_back(u);
        adj[u].push_back(v);
    }
    auto it = max_element(deg.begin(), deg.end());
    // if (*it <= 2) {
    //     cout << *it - 1 << endl;
    //     return;
    // }

    int start = it - deg.begin();

    function<int(int)> dfs = [&] (int node) {
        vis[node] = 1;
        if (deg[node] == 1) {
            return 1;
        }
        int res = 0;
        for (auto nei: adj[node]) {
            if (vis[nei] == 0) {
                res += dfs(nei);
            }
        }
        return res;
    };

    int ans = dfs(start);
    for (auto nei: adj[start]) {
        if (deg[nei] == 1)  {
            ans--;
        }
    }
    cout << ans << endl;




    // queue<int> que;
    // for (int node = 1; node <= n; node++) {
    //     if (deg[node] == 1) {
    //         que.push(node);
    //         val[node] = 1;
    //     }
    // }

    // int last = 0;

    // while (!que.empty()) {

    //     int sz = que.size();
    //     for (int i = 0; i < n; i++) {
    //         int node = que.front();
    //         que.pop();
    //         last = node;

    //         for (auto nei: adj[node]) {
    //             ind[nei]--;
    //             val[nei] += val[node];
    //             if (ind[nei] == 1) {
    //                 que.push(nei);
    //             }
    //         }
    //     }
    // }

    // cout << "lasst: " << last << endl;
    // for (auto nei: adj[last]) {
    //     if (deg[nei] == 1) {
    //         val[last]--;
    //     }
    // }
    // cout << val[last] << endl;
    
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t = 1;
    cin >> t;
    
    while (t--) {
        solve();
    }
    
    return 0;
}