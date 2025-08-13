#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

const int MOD = 1e9 + 7;

void solve() {
    int n; cin >> n;
    vector<string> grid(n);
    for(auto &row: grid) cin >> row;

    vector<vector<int>> dp(n + 1, vector<int>(n + 1));
    if (grid[0][0] == '.'){
        dp[1][0] = 1;
    }
    for (int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            if (grid[i - 1][j - 1] == '.'){
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MOD;
            }
        }
    }
    cout << dp[n][n] << '\n';
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