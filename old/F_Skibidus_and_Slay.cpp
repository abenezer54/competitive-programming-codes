#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;


void solve() {
    int n; cin >> n;
    // cout << n << '\n';
    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++){
        cin >> a[i];
    }

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; i++){
        int x, y; cin >> x >> y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }

    vector<int> ans(n + 1, 0);
    for (int node = 1; node <= n; node++){
        map<int, int> cnt;
        for (auto nei: adj[node]){
            if (a[node] == a[nei]){
                ans[a[node]] = 1;
            }
            cnt[a[nei]] += 1;
        }
        for (auto& [k, v]: cnt){
            if (v > 1) {
                ans[k] = 1;
            }
        }
    }

    for (int node = 1; node <= n; node++){
        cout << ans[node];
    }

    cout << '\n';
   
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