#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll n, q, k; cin >> n >> q >> k;
    vector<ll> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    a.push_back(k + 1);
    a.insert(a.begin(), 0);

    vector<ll> dp(n + 2);
    for (int i = 1; i <= n; i++) {
        ll left = a[i] - a[i - 1] - 1;
        ll right = a[i + 1] - a[i] - 1;
        dp[i] = left + right;

    }
    // cout << dp << endl;
    for (int i = 1; i <= n + 1; i++) {
        dp[i] += dp[i - 1];
    }
    // cout << dp << endl;

    for (int i = 0; i < q; i++) {
        int l, r; cin >> l >> r;
        ll left = a[l] - 1;
        if (l != r) left += a[l + 1] - a[l] - 1;
        
        ll right = k - a[r];
        if (l != r) right += a[r] - a[r - 1] - 1;
        
        ll ans = right + left;
        if (r - l > 1) {
            ans += dp[r - 1] - dp[l];
        }
        cout << ans << endl;

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