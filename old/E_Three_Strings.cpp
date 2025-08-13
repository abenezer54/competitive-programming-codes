#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    string a, b, c;
    cin >> a; int n = a.size();
    cin >> b; int m = b.size();
    cin >> c;


    vector<vector<int>> dp(n + 5, vector<int>(m + 5, INT_MAX));
    dp[0][0] = 0;
    for (int i = 0; i <= n; i++){
        for (int j = 0; j <= m; j++){
            int c_idx = i + j;
            if (i + 1 <= n){
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + (a[i] != c[c_idx]));
            }

            if (j + 1 <= m) {
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + (b[j] != c[c_idx]));
            }
        }
    }


    cout << dp[n][m] << endl;
   
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