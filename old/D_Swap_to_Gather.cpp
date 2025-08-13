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
    string s; cin >> s;
    vector<ll> idx;
    for (ll i = 0; i < n; i++) {
        if (s[i] == '1'){
            idx.push_back(i);
        }
    }
    ll midx = idx.size() / 2;
    ll mid = idx[midx];
    ll x = midx;
    ll y = 1;
    ll ans = 0;
    for (ll i = 0; i < idx.size(); i++) {
        if (i <= midx) {
            ll ex = mid - x--;
            ans += ex - idx[i];
        } else {
            ll ex = mid + y++;
            ans += idx[i] - ex;
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