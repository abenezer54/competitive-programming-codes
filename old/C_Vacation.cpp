#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;
const int INF = 1e9;

void solve() {
    int n; cin >> n;
    vector<array<ll, 3>> a(n);
    for (int i = 0; i < n; i++ ) {
        cin >> a[i][0] >> a[i][1] >> a[i][2];
    }
    
    
    vector<array<ll, 3>> dp(n, array<ll, 3>{INF});
    dp[0] = a[0];

    for (int i = 1; i < n; i++) {
        dp[i][0] = a[i][0] + max(dp[i - 1][1], dp[i - 1][2]);
        dp[i][1] = a[i][1] + max(dp[i - 1][0], dp[i - 1][2]);
        dp[i][2] = a[i][2] + max(dp[i - 1][0], dp[i - 1][1]);
    }
    cout << *max_element(dp[n - 1].begin(), dp[n - 1].end()) << endl;
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