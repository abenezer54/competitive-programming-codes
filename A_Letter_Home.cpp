#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, s; cin >> n >> s;
    int mn = 1000, mx = 0;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        mn = min(mn, x);
        mx = max(mx, x);
    }
    int d = min(abs(s - mx), abs(s - mn));
    cout << mx - mn + d << endl;
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