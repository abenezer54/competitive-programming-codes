#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll n, k; cin >> n >> k;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];

    ll m = n / (k + 1);
    vector<ll> dp(n + 1, 0);

    for (ll i = n - k - 1; i >= 0; i--) {
        dp[i] = max(dp[i + 1], a[i] + dp[i + k + 1]);

    }
    cout << *max_element(dp.begin(), dp.end()) << endl;
   
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