#include "bits/stdc++.h"
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;
const ll INF = LLONG_MAX; 

void solve() {
    int n, m, X;
    cin >> n >> m >> X;
    vector<vector<int>> adj1(n + 1);
    vector<vector<int>> adj2(n + 1);

    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        adj1[u].push_back(v);
        adj2[v].push_back(u);
    }

    priority_queue<array<ll, 3>, vector<array<ll, 3>>, greater<>> pq;
    vector<ll> dist(n + 1);

    pq.push({0LL, 1LL, 0LL});
    pq.push({X, 1, 1});
    vector<int> vis1(n + 1, 0);
    vector<int> vis2(n + 1, 0);



    while (!pq.empty()) {
        array<ll, 3> top = pq.top();
        pq.pop();
        ll w = top[0], node = top[1];
        ll type = top[2];
        if (type == 0) {
            if (vis1[node]) continue;
            vis1[node] = 1;
        } else {
            if (vis2[node]) continue;
            vis2[node] = 1;
        }

        if (node == n) {
            cout << w << endl;
            return;
        }
        
        if (type == 0) {
            pq.push({w + X, node, 1});
        } else {
            pq.push({w + X, node, 0});
        }

        for (int nei: adj1[node]) {
            if (type == 0) {
                pq.push({w + 1, nei, 0});
            } 
        }
        for (int nei: adj2[node]) {
            if (type == 1) {
                pq.push({w + 1, nei, 1});
            }
        }
    }
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
