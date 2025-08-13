#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll k; cin >> k;
    ll tot = 0; 
    ll x = -1e9;
    vector<array<ll, 2>> ans;
    ll y = x + 1;
    while (tot != k) {
        ll cnt = 0;
        while (tot + cnt <= k) {
            ans.push_back({x, y});
            tot += cnt;
            cnt++;
            y++;
        }

        x++;
    }

    cout << ans.size() << endl;
    for (auto&[x, y]: ans) {
        cout << x << ' ' << y << endl;
    }
   
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