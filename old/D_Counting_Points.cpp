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
    vector<ll> x(n), r(n); 
    for (int i = 0; i < n; i++) {
        cin >> x[i];
    }
    for (int i = 0; i < n; i++) {
         cin >> r[i];
    }
 
    ll ans = 0;
    map<int, int> mx;

    // cout << x << endl;
    for (ll i = 0; i < n; i++) {
        for(ll xx = x[i] - r[i]; xx <= x[i] + r[i]; xx++) {
            ll xln = (xx - x[i]) * (xx - x[i]);
            ll max_y = sqrt(r[i] * r[i] - xln);
            // cout << "xx " << xx << ' ' << max_y << endl;
            if (!mx.count(xx)) {
                ans += ((max_y * 2) + 1);
                mx[xx] = max_y; 
            } else if (max_y > mx[xx]){
                ans -= (mx[xx] * 2) + 1;
                ans += (max_y * 2) + 1;
                mx[xx] = max_y;
            }
        }
        // cout << i << ' ' << ans << endl;
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