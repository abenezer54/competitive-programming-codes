#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n, r; cin >> n >> r;
    int remain = 0;
    int ans = 0;
    for (int i = 0; i < n; i ++){
        int cur; cin >> cur;
        int hv = cur / 2;
        int rr = cur % 2;
        int used = min(r, hv);
        r -= used;
        ans += 2 * used;
        remain +=( hv )- (used);
        remain += rr;
    }
    // cout << "remain " << remain << ' ' << r << '\n';
    if (remain <= r){
        ans += remain;
    }
    else {
        remain -= r;
        int x = r -  remain;
        ans += x;
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