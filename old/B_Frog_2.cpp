#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, k; cin >> n >> k;
    
    vector<int> h(n);
    for (int i = 0; i < n; i++) {
        cin >> h[i];
    }

    vector<int> dp(n, 1e9);
    dp[0] = 0;

    for (int i = 1; i < n; i++) {
        for (int j = i - 1; j >= max(0, i - k); j--) {
            dp[i] = min(dp[i], abs(h[i] - h[j]) + dp[j]);
        }
    }

    cout << dp[n - 1] << endl;
   
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