#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

long long binpow(long long a, long long b, long long m) {
    a %= m;
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}

void solve() {
    int n; cin >> n;
    vector<int>a(n);
    vector<int>b(n);
    vector<int>d(n);
    vector<vector<int>> adj(n + 1);
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    for(int i = 0; i < n; i++){
        cin >> b[i];
    }
    for(int i = 0; i < n; i++){
        cin >> d[i];
    }

    vector<int> start;
    for (int i = 0; i < n; i++){
        if (d[i] == 0 && a[i] != b[i]){
            adj[a[i]].push_back(b[i]);
            // adj[b[i]].push_back(a[i]);
            start.push_back(a[i]);
            start.push_back(b[i]);
        }
    }
    // cout << adj<< endl;
    vector<int> col(n + 1, 0);
    int cycle = 0;
    function<void(int, int)> dfs = [&](int node, int parent) {
        col[node] = 1;
        for (int nei: adj[node]){
            if (col[nei] == 1){
                cycle++;
            }
            if (nei != parent && col[nei] == 0){
                dfs(nei, node);
            }
        }
        col[node] = 2;
    };
    
    if (start.size() != 0){
        for (auto val: start){
            if (col[val] == 0){
                dfs(val, -1);
            }
        }
    }
    int ans = binpow(2, cycle, MOD);
    cout << ans << '\n';

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