#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, m; cin >> n >> m;
    vector<int> a(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }

    vector<ll> p(n, 0);
    for (int i = 1; i < n; i++){
        p[i] += p[i - 1] + max(0, a[i - 1] - a[i]);
    }

    vector<ll> s(n, 0);
    for (int i = n - 2; i >= 0; i--) {
        s[i] += s[i + 1] + max(0, a[i + 1] - a[i]);
    }

    for (int i = 0; i < m; i++) {
        int x, y; cin >> x >> y;
        if (x < y) {
            ll val = p[y - 1] - p[x - 1];
            cout << val << "\n";
        } else {
            ll val = s[y - 1] - s[x - 1];
            cout << val << "\n";
        }
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