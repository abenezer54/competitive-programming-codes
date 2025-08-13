#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll n; cin >> n; 
    ll p = 63 - __builtin_clzll(n);
    ll ans = 0LL;

    for (int i = 1; i <= p; i++) {
        ll val = 1LL << i;
        ll sq_limit = sqrtl((long double)n / val);  
        ans += (sq_limit + 1) / 2; 
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