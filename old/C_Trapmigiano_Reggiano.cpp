#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, start, end; 
    cin >> n >> start >> end;
    vector<vector<int>> adj(n + 1);
    cout << adj << endl;
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >>  v;

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    queue<int> que;
    que.push(start);
    vector<int> vis(n + 1);
    vector<int> p(n + 1, -1);
    vis[start] = 1;
    int d = 0;
    while (!que.empty()) {
        int sz = que.size();
        for (int i = 0; i < sz; i++) {
            int node = que.front(); 
            que.pop();
            if (node == end) {
                break;
            }
            
            for (auto nei: adj[node]) {
                if (vis[nei] == 0) {
                    que.push(nei);
                    vis[nei] = 1;
                    p[nei] = node;
                }
            }
        }
        d++;
    }
    set<int> path;
    path.insert(end);
    auto cur = end;
    while (p[cur] != -1) {
        path.insert(p[cur]);
        cur = p[cur];
    }


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