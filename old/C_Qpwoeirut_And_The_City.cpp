#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n; cin >> n;
    vector<int> h(n);
    for (int i = 0; i < n; i++){
        cin >> h[i];
    }
    vector<ll> dp(n, 1e9);
    dp[0] = 0;
    dp[1] = max(0, max(h[0], h[2]) - h[1] + 1);
    for (int i = 1; i < n - 1; i++){
        ll cur = max(0, max(h[i - 1], h[i + 1]) - h[i] + 1);
        
        for (int j = 2; j <= 3; j++){
            if (i - j >= 0){
                dp[i] = min(dp[i], cur + dp[i - j]);
            }
        }
    }
    // cout << dp << endl;
    cout << dp[n - 2] << endl;
   
    
    
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