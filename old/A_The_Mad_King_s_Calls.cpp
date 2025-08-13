#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;


void solve() {
    int x; cin >> x;
    int val = x % 10;
    int ans = 10 * (val - 1);
    int sz = to_string(x).size();
    for (int i = 1; i <= sz; i++) {
        ans += i;
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