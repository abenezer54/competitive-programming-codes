#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int a, b; cin >> a >> b;
    int x, y; cin >> x >> y;
    int d1 = abs(a - x);
    int d2 = abs(b - y);
    int mn = min(d1, d2);
    cout << mn + (d1 - mn) + (d2 - mn) << endl;
   
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