#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n, k; cin >> n >> k;
    vector<vector<int>> adj(n + 1, vector<int>());
    vector<int> ind(n + 1);
    for(int i = 0; i < n - 1; i++){
            int u, v; cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
            ind[v]++;
            ind[u]++;
    }
    if (n == 1){
        cout << 0 << endl;
        return;
    }
    
    deque<int> que;
    vector<bool> vis(n + 1, false);
    for (int v = 1; v <= n; v++){
        if (ind[v] == 1){
            que.push_back(v);
            vis[v] = true;
        }
    }

    int cnt = n;
    while (k-- && !que.empty()){
        int ln = que.size();
        for(int i = 0; i < ln; i++){
            int node = que.front();
            que.pop_front();
            cnt--;
            for(auto nei: adj[node]){
                ind[nei]--;
                if (ind[nei] == 1 && !vis[nei]){
                    que.push_back(nei);
                    vis[nei] = true;
                }
            }
        }

    }

    cout << cnt << endl;



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