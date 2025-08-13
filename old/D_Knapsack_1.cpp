#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n, W; cin >> n >> W;
    vector<int> weight(n);
    vector<int> val(n);
    for(int i = 0; i < n; i++){
        cin >> weight[i] >> val[i];
    }
    ll dp[100005];
    // vector<ll> dp(W + 1);
    for (int i = 0; i < n; i ++){
        for(int j = int(1e5) + 5; j >= 0; j--){
            if(j - weight[i] >= 0){
                dp[j] = max(dp[j], dp[j - weight[i]] + val[i]);
            }
        }
    }
    cout << dp[W] << '\n';
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