#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;


void solve() {
    int n; cin >> n;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    vector<ll> s(n, 0);
    for (ll i = n - 2; i >= 0; i--){
        s[i] += s[i + 1] + (abs(a[i] - a[i + 1]) * (n - (i + 1)));
    }
    
    // cout << s << "\n";
    vector<ll> p(n, 0);
    for (ll i = 1; i < n; i++){
        p[i] += p[i - 1] + (abs(a[i] - a[i - 1]) * i);
    }
    // cout << p << "\n";
    ll res = 0;

    ll ans = 1e18;
    for (ll i = n - 1; i >= 0; i--){
        if (s[i] + p[i] <= ans){
            ans = s[i] + p[i];
            res = a[i];
        }

    }
    cout << res << "\n";
    
    

   
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