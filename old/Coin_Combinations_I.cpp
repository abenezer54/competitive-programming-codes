#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

const int MOD = 1e9 + 7;

void solve() {
    int n, x; cin >> n >> x;
    vector<int> c(n);
    for(auto &x: c) cin >> x;

    vector<int> dp(x + 1, 0);
    dp[0] = 1;
    for(int num = 1; num <= x; num++){
        for(auto coin: c){
            if(num - coin >= 0){
                dp[num] = (dp[num] + dp[num - coin]) % MOD;
            }
        }
    }

    cout << dp[x] << '\n';

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