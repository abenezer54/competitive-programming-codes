#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n; cin >> n;
    vector<int> a(n + 1);
    for (int i = 1; i <=n; i++) cin >> a[i];
    vector<vector<int>> adj(n + 1);

    for (int i = 1; i <=n; i++){
        if (a[i] != i){
            adj[i].push_back(a[i]);
            adj[a[i]].push_back(i);
        }
    }



    vector<int> col(n + 1);
    int cycles = 0;
    function<void(int, int)> dfs = [&] (int node, int par){
        col[node] = 1;

        for (int nei: adj[node]){
            if (par == nei) continue;

            if (col[nei] == 0){
                dfs(nei, node);
            }
            if (col[nei]  == 1){
                cycles++;
            }
        }
        col[node] = 2;
    };

    int comp = 0;

    for (int i = 1; i <= n; i++){
        if (col[i] == 0){
            dfs(i, -1);
            comp++;
        }
    }

    int mn = cycles;
    if (cycles < comp){
        mn++;
    }
    int mx = comp;
    // cout << comp << endl;
    
    cout << mn << ' ' << mx << endl;
   
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