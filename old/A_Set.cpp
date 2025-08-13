#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    ll l, r, k; cin >> l >> r >> k;
    ll right = r + 1;
    ll left = l;
    // r++;

    while (left  + 1 < right){
        ll  mid = left + (right - left) / 2;
        // cout << "mid here " <<mid << ' ' << k << endl;
        if (mid * k <= r)
            left =  mid;
        else
            right = mid;
    }
    ll ans = left - l + 1;
    if (l * k > r)
        ans = 0;
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