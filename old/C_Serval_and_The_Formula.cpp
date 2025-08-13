#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll x, y; cin >> x >> y;
    if (x == y) {
        cout << -1 << endl;
        return;
    }
    ll k = 0LL;
    for (int i = 0; i < 32; i++) {
        ll prevx = 0, prevy = 0;
        for (int j = i - 1; j >= 0; j--) {
            if ((x & (1 << j))) {
                prevx += (1 << j);
            }
            if (y & (1 << j)) {
                prevy += (1 << j);
            }
        }
        if ((x & (1 << i)) && (y & (1 << i))) {
            ll rem = (1 << i) - (max(prevy, prevx));
            k += rem;
            x += rem;
            y += rem;

        }
    }
    cout << k << endl;
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