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
        for (int i = 0; i < n; i++) cin >> a[i];

        vector<int> dp(n + 1, INT_MAX);
        dp[n] = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (i + a[i] + 1 <= n) {
                dp[i] = min(dp[i], dp[i + a[i] + 1]);
            }
            dp[i] = min(dp[i], dp[i + 1] + 1);
        }

        cout << dp[0] << endl;
    
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