#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll n, m; cin >> n >> m;

    vector<vector<array<ll, 2>>> adj(n + 1);

    for (int i = 0; i < m; i++) {
        ll u, v; cin >> u >> v;
        ll w; cin >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    vector<int> vis(n + 1);

    function<ll(ll, ll)> backtrack = [&] (ll node, ll prev) {
        if (node == n) return prev;
        vis[node] = 1;

        ll res = LLONG_MAX;
        for (auto[nei, w]: adj[node]) {
            if (vis[nei] == 0) {
                res = min(res, backtrack(nei, prev ^ w));
            }
        }
        vis[node] = 0;
        return res;
    };


    cout << backtrack(1, 0LL) << endl;
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