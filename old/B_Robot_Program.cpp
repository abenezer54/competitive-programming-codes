#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll n, x, k; cin >> n >> x >> k;
    string s; cin >> s;
    ll ans = 0;
    bool flag = false;

    for (ll i = 0; i < n; i++) {
        k--;
        if (s[i] == 'L') {
            x--;
        } else {
            x++;
        }
        if (x == 0) {
            ans++;
            flag = true;
            break;
        }
    }
    
    if (!flag) {
        cout << ans << endl;
        return;
    }

    ll left = 0, right = 0;
    ll kk = k;
    for (ll i = 0; i < min(n, kk); i++) {
        k--;
        left += s[i] == 'L';
        right += s[i] == 'R';
        if (left == right) {
            ans++;
            ans += k / (i + 1);
            break;
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