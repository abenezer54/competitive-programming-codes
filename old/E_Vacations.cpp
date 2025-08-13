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
    vector<array<int, 3>> dp(n + 1, {INT_MAX, INT_MAX, INT_MAX});
    dp[0] = {0, 0, 0};
    
    for (int i = 0; i < n; i++) {
        if (a[i] & 1) {
            int temp = (i > 0 ? dp[i - 1][0]: 0);
            dp[i + 1][0] = min({dp[i + 1][0], dp[i][1], temp});
        } // else {
        //     dp[i + 1][0] = min({dp[i + 1][0], dp[i][1], dp[i][2], dp[i][0]});
        // }

        if (a[i] & 2) {
            int temp = (i > 0 ? dp[i - 1][1]: 0);
            dp[i + 1][1] = min({dp[i + 1][1], dp[i][0], temp});
        } // else {
        //     dp[i + 1][1] = min({dp[i + 1][1], dp[i][1], dp[i][2], dp[i][0]});
        // }
        dp[i + 1][2] = min({dp[i][0], dp[i][1], dp[i][2]}) + 1;
    }
    cout << dp << endl;
   
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