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
    for (int i = 0; i < n - 1; i++) {
        int x, y; cin >> x >> y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }

    set<int> colors;
    for (int i = 1; i <= n; i++) {
        colors.insert(i);
    }

    queue<int> que;
    que.push(1);
    vector<int> vis(n + 1);
    vis[1] = 1;
    vector<int> ans(n + 1), par(n + 1, -1);
    vector<int> prev;
    int max_color = 1;
    
    while (!que.empty()) {
        int sz = que.size();
        
        vector<int> temp;
        
        for (int i = 0; i < sz; i++) {
            int node = que.front(); que.pop();
            temp.push_back(node);
            auto it = colors.begin();
            auto cur_color = *it;
            if (node == 1) {
                cout << "cur " << cur_color << endl;
            }
            if (node != 1 && cur_color == ans[par[node]]) {
                int pp = cur_color;
                colors.erase(it);
                auto it2  = colors.begin();
                cur_color = *it2;
                colors.insert(pp);
                colors.erase(it2);
                cout << "node: " << node << ' ' << cur_color << endl;
            } else {
                colors.erase(it);
            }
            
            ans[node] = cur_color;
            max_color = max(max_color, cur_color);
            for (auto nei: adj[node]) {
                if (vis[nei] == 0) {
                    vis[nei] = 1;
                    que.push(nei);
                    par[nei] = node;
                }
            }
        }

        for (auto v: temp) {
            colors.insert(v);
        }
    }
    cout << max_color << endl;
   
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