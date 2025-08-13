#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    ll n, m; cin >> n >> m;
    vector<ll> a(n);
    for (auto& x: a){
        cin >> x;
    }
    ll b; cin >> b;

    a[0] = min(a[0], b - a[0]);
    for (ll i = 1; i < n; i++){
        ll mn = min(a[i], b - a[i]);
        ll mx = max(a[i], b - a[i]);
        if (mn >= a[i - 1]){
            a[i] = mn;
        } else {
            a[i] = mx;
        }
    }
    for (ll i = 1; i < n; i++){
        if (a[i] < a[i - 1]){
            cout << "NO" << '\n';
            return;
        }
    }
    // cout << a << '\n';
    cout << "YES" << '\n';
    
   
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