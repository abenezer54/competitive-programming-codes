#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n; cin >> n;
    const int MOD = 1e9 + 7;
    vector<int> dp(n + 1);
    dp[0] = 1;

    for (int i = 1; i <= n; i++){
        for(int j = 1; j <= 6; j++){
            if (i - j >= 0){
                dp[i] += dp[i - j];
                dp[i] %= MOD;
            } 
        }
    }
    cout << dp[n] << '\n';
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