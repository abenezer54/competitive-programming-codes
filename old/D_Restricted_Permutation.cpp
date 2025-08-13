#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, m;  cin >> n >> m;
    vector<int> ind(n + 1), ans;
    priority_queue<int> pq;
    vector<vector<int>> adj(n + 1);

    for (int j = 0; j < m; j++) {
        int a, b; cin >> a >> b;
        ind[b]++;
        adj[a].push_back(b);
    }

    for (int node = 1; node <= n; node++) {
        if (ind[node] == 0) {
            pq.push(-node);
        }
    }
    
    while (!pq.empty()) {
        int sz = pq.size();
        for (int i = 0; i < sz; i++) {
            int node = -pq.top(); pq.pop();
            ans.push_back(node);
            for (int nei: adj[node]) {
                ind[nei]--;
                if (ind[nei] == 0) {
                    pq.push(-nei);
                }
            }
        }
    }
   
    if (ans.size() != n) {
        cout << "-1\n";
        return;
    } 
    for (int val : ans) {
        cout << val << ' ';
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