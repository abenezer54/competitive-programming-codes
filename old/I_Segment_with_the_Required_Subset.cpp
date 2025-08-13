#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;
// 1825443758183472130

void solve() {
    // for (int i = 0; i < 1e3; i++){
    //     cout << 2 << ' ';
    // } 
    int n, s; cin >> n >> s;
    ll dp[1005];
    memset(dp, 0, sizeof(dp));
    dp[0] = 1;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    int l = 0;
    int ans = 1e9;
    for (int r = 0; r < n; r++){
        // cout << "r " << r << endl;
        for (int j = 1000; j >= 0; j--){
            if (dp[j] > 0 && (j + a[r] <= 1000)){
                dp[j + a[r]] += dp[j];
                dp[j + a[r]] %= MOD;
            }
        }
        // cout << dp[s] << endl;

        while (dp[s] > 0) {
            for (int j = 0; j <= 1000; j++){
                if (j + a[l] <= 1000){
                    dp[j + a[l]] -= dp[j];
                    dp[j + a[l]] = ((dp[j + a[l]] % MOD) + MOD) % MOD;
                }
            }
            ans = min(ans, r - l + 1);
            l++;
        }
    }
    // cout << dp[128]<< endl;
    if (ans == 1e9){
        cout << "-1\n";
    } else {
        cout << ans << '\n';
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