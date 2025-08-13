#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll n; cin >> n;
    vector<vector<array<ll, 2>>> adj(n + 1);
    ll ans = 0LL;
    for (ll i = 0; i < n - 1; i++) {
        ll u, v, w; cin >> u >> v >> w;
        adj[v].push_back({u, w});
        adj[u].push_back({v, w});
        ans += (ll) 2 * w;
    }
    vector<ll> vis(n + 1);

    function<ll(ll)> dfs = [&] (ll node) {
        vis[node] = 1;
        ll mx = -1;
        for (auto [nei, w]: adj[node]) {
            if (vis[nei] == 0) {
                mx = max(mx, dfs(nei) + w);
            }
        }
        if (mx == -1) {
            return 0LL;
        }
    
        return mx;
    };
    
    ans -= dfs(1);
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