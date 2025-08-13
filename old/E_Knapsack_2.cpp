#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    ll n, W; cin >> n >> W;
    vector<ll> weight(n);
    vector<ll> val(n);
    for(ll i = 0; i < n; i++){
        cin >> weight[i] >> val[i];
    }

    vector<ll> dp(n * 1000 + 5, -1);
    dp[0] = 0;

    for (ll i = 0; i < n; i ++){
        for(ll j = dp.size() - 1; j >= 0; j--){
            if(j - val[i] >= 0 and dp[j - val[i]] != -1){
                if (dp[j] == -1)
                    dp[j] = dp[j - val[i]] + weight[i];
                else 
                    dp[j] = min(dp[j], dp[j - val[i]] + weight[i]);
            }
        }
    }


    ll ans = 0;
    for (ll i = 1; i < dp.size(); i++){
        if (dp[i] <= W && dp[i] != -1) {
            ans = i;
        }
    }

    cout << ans << '\n';
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    ll t = 1;
    // cin >> t;
    
    while (t--) {
        solve();
    }
    
    return 0;
}