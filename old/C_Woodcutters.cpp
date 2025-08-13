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
    vector<array<int, 2>> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i][0];
        cin >> a[i][1];
    }
    if (n == 1) {
        cout << 1 << endl;
        return;
    }
    int ans = 2;
    int prev = a[n - 1][0];

    for (int i = n - 2; i > 0; i--) {
        if (a[i][0] + a[i][1] < prev) {
            ans++;
            prev = a[i][0];
        } else if (a[i][0] - a[i][1] > a[i - 1][0]) {
            ans++;
            prev = a[i][0] - a[i][1];
        } else {
            prev = a[i][0];
        }
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