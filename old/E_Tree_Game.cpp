#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
// #define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n; cin >> n;
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    unordered_set<vector<int>> arr;
    for (int start = 1; start <= n; start++) {
        int move = 0;
        queue<int> q; q.push(start);
        vector<int> vis(n); vis[start] = 1;

        while (!q.empty()) {
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                int node = q.front(); q.pop();
                if (move & 1 && move > 1) {
                   
                }
            }
            move++;
        }
    }

    int step = 1;
    if (arr.size() & 1) {
        cout << "First" << endl;
    }else {
        cout << "Second" << endl;
        step = 0;
    }

    while (true) {
        if (step & 1) {
            arr.
        } else {

        }

        step++;
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