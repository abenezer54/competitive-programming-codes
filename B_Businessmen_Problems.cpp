#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    map<int, int> mx;
    int n; cin >> n;
    for (int i = 0; i < n; i++) {
        int a, x; cin >> a >> x;
        mx[a] = max(mx[a], x);
    }
    int m; cin >> m;
    for (int i = 0; i < m; i++) {
        int a, x; cin >> a >> x;
        mx[a] = max(mx[a], x);
    }
    ll ans = 0ll;
    for (auto [_, val] : mx) {
        ans += val;
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