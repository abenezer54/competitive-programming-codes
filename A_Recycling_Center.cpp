#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll n, c; cin >> n >> c;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) {
        cin >> a[i];   
    }


    sort(a.rbegin(), a.rend());
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] <= c) {
            for (int j = i + 1; j < n; j++) {
                a[j] *= 2;
            }
        } else {
            ans++;
        }
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