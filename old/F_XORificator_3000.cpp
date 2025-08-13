#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

ll xor_(ll n){
    if (n % 4 == 0)
        return n;
    if (n % 4 == 1)
        return 1;
    if (n % 4 == 2)
        return n + 1;
    return 0;
}

ll xor_range(ll l, ll r){
    return xor_(r) ^ xor_(l - 1);
}

void solve() {
    ll l, r, i, k; cin >> l >> r >> i >> k;

    ll ans = xor_range(l,  r); // calculate the total xor [l, r]

    ll right = (r - k) >> i; // divide by 2^i to change them to the chunks
    ll left = (l - k + (1 << i) - 1) >> i; // divide by 2^i and add (2^i - 1 to round up to real index or chunk)

    ll cnt_of_uninteresting_numbers = right - ((l - k - 1) >> i); // -1 in the case of l - k == k
    
    ans ^= (xor_range(left, right) << i); // double xor the xor of uniteresting numbers
    if (cnt_of_uninteresting_numbers & 1){
        ans ^= k;
    }
    cout << ans << '\n';
    
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