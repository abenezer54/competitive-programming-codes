#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, k; cin >> n >> k;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    vector<ll> s(n);
    s[n - 1] = a[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        s[i] = (ll) s[i + 1] + a[i];
    }

    ll ans = s[0];
    s.erase(s.begin());
    sort(s.rbegin(), s.rend());
    
    for (int i = 0; i < k - 1; i++) {
        ans += s[i];
    }
    cout << ans << endl;
   
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