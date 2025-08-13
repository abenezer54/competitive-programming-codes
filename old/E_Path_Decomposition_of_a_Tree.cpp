#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, k; cin >> n >> k;
    vector<int> ind(n * k + 1);
    vector<vector<int>> adj(n * k + 1);
    for (int i = 0; i < n * k - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        ind[v]++; ind[u]++;
    }
    if (k == 1) {
        cout << "Yes" << endl;
        return;

    }

    queue<int> que;
    for (int node = 1; node <= n * k; node++) {
        if (ind[node] == 1) {
            que.push(node);
        }
    }
    

    map<int, vector<int>> mp;
    while (!que.empty()) {
        int node = que.front();
        que.pop();
        ll sm = accumulate(mp[node].begin(), mp[node].end(), 1LL);
        // cout << "node: " << node << " sm: " << sm << endl;
        if (sm > k) {
            cout << "No" << endl;
            return;
        }

        if (mp[node].size() == 2 && sm != k) {
            cout << "No" << endl;
            return;
        }

        if (mp[node].size() > 2) {
            cout << "No" << endl;
            return;
        }

        for (auto nei: adj[node]) {
            ind[nei]--;
            if (ind[nei] == 1) {
                que.push(nei);
            }
            if (sm % k > 0) mp[nei].push_back(sm % k);
            // cout << "nei: " << nei << endl;
        }
    }
    cout << "Yes" << endl;
   
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