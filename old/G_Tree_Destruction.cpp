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
    vector<vector<int>> adj(n + 1);
    vector<int> ind(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        ind[u]++; ind[v]++;
    }
    auto deg = ind;
    queue<int> que;
    
    for (int node = 1; node <= n; node++) {
        if (ind[node] == 1) {
            que.push(node);
        }
    }
    
    vector<3earray<int, 2>> mx_prev(n + 1);
    int ans = *max_element(deg.begin(), deg.end());

    while (!que.empty()) {
        int node = que.front();
        que.pop();

        int cur_mx = max(mx_prev[node][0] + deg[node] - 2, deg[node] - 1);
        ans = max(ans, mx_prev[node][1] + mx_prev[node][0] + deg[node] - 2);
        ans = max(ans, mx_prev[node][0] + deg[node] - 1);
        
        for (int nei: adj[node]) {
            
            vector<int> temp = {cur_mx, mx_prev[nei][0], mx_prev[nei][1]};
            sort(temp.begin(), temp.end());
            mx_prev[nei][0] = temp[2];
            mx_prev[nei][1] = temp[1];
            
            ind[nei] -= 1;
            if (ind[nei] == 1) {
                que.push(nei);
            }
        }
    }
    cout << ans << endl;
 
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