#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll n, m; cin >> n >> m;
    cout << log2(400) << endl;
    ll ans = 0;
    for (ll i = 0; i <= m; i++) {
        ans += pow(n, i);
        if (ans > 1e9) {
            cout << "inf" << endl;
            return;
        }
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