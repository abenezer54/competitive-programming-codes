#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n; cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    map<int, int> mp;
    int ans = MOD;
    for (int i = 0; i < n; i++) {
        if (mp.count(a[i])) {
            ans = min(ans, i - mp[a[i]] + 1);
        } 
        mp[a[i]] = i;
    }

    
    if (ans == MOD) {
        cout << -1 << endl;
    } else {
        cout << ans << endl;
    }
   
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