#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll m, k, a1, ak; cin >> m >> k >> a1 >> ak;
    ll d;
    d = m / k;
    m -= min(ak * k, d * k);
    if (m <= a1) {
        cout << 0 << endl;
        return;
    }
    ll dd = m / k;
    ll r = m % k;
    ll x = min(r, a1);
    r -= x;
    a1 -= x;
    dd -= a1 / k;
    cout << dd + r << endl;
  
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