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
    set<pair<int, int>> vis;
    int ans = 0;
    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        if (u == v) {
            ans++;
            continue;
        }
        pair<int, int> p = {min(u, v), max(u, v)};
        if (vis.count(p)) ans++;
        vis.insert(p);
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