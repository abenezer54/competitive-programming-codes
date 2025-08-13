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
    vector<ll> A(n), B(n);
    for (ll i = 0; i < n; i++){
        cin >> A[i];
        A[i] %= m;
    }
    for (ll i = 0; i < n; i++){
        cin >> B[i];
        B[i] %= m;
    }

    multiset<ll> ms(B.begin(), B.end());
    ll ans = 0;
    for (ll i = 0; i < n; i++) {
        auto p = ms.lower_bound(m - A[i]);
        if (p == ms.end()) p = ms.begin();
        ans += (A[i] + *p) % m;
        ms.erase(p);
    }
    cout << ans << endl;


   
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