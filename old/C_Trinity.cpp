#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n; cin >> n;
    vector<int> a(n);
    for (auto &x: a) cin >> x;
    sort(a.begin(), a.end());
    // cout << a << endl;
    ll ans = n;
    for (ll i = 0; i < n - 2; i++){
        auto cnt = n - (upper_bound(a.begin(), a.end(), a[i] + a[i + 1] - 1) - a.begin());
        ans = min(ans, cnt + i);
    }
    cout << ans << endl;

    
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    ll t = 1;
    cin >> t;
    
    while (t--) {
        solve();
    }
    
    return 0;
}