#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int INF = 1e9;

void solve() {
    int n; cin >> n;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++){
        cin >> a[i];
    }

    vector<int> ans(n + 1, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, 1});

    while (!pq.empty()){
        auto [weight, node] = pq.top();
        pq.pop();
        
        if (weight >= ans[node]) continue;

        ans[node] = weight;
        pq.push({weight + 1, a[node]});
        if (node + 1 <= n) pq.push({weight + 1, node + 1});
        if (node > 1) pq.push({weight + 1, node - 1});
    }
    
    for (int i = 1; i <= n; i++){
        cout << ans[i] << ' ';
    }
    cout << '\n';
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