#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll n, x, y; cin >> n >> x >> y;
    vector<vector<ll>> adj(n + 1);
    for (ll i = 0; i < n - 1; i++) {
        ll a, b; cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    vector<ll> vis(n + 1);
    vector<ll> par(n + 1, -1);

    function<void(ll)> dfs = [&] (ll node) {
        if (node == y) return; 
        vis[node] = 1;
        for (auto nei: adj[node]) {
            if (vis[nei] == 0) {
                par[nei] = node;
                dfs(nei);
            }
        }
    };

    function<ll(ll)> dfs2 = [&] (ll node) {
        vis[node] = 1;
        ll sz = 1;
        for (auto nei: adj[node]) {
            if (vis[nei] == 0) {
                par[nei] = node;
                sz += dfs2(nei);
            }
        }
        return sz;
    };


    dfs(x);
    vector<ll> path;
    ll cur = y;
    while (par[cur] != -1) {
        path.push_back(cur);
        cur = par[cur];
    }
    path.push_back(x);



    vis.assign(n + 1, 0);
    for (auto node: path) {
        vis[node] = 1;
    }

    ll left =  dfs2(x);
    ll right = dfs2(y);

    ll ans = (ll) n * (n - 1);
    ans -= (ll) left * right;
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