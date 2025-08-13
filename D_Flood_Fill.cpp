#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

const int MAXN = 5005; 
int memo[MAXN][MAXN][2];

void solve() {
    int n; cin >> n; 
    vector<int> a(n);
    
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    memset(memo, -1, sizeof(memo));
    
    function<int(int, int, int)> dp = [&] (int l, int r, int x) {
        if (l >= r) {
            return 0;
        }

        if (memo[l][r][x] != -1) {
            return memo[l][r][x];
        }
        
        int val = 0;
        if (x == 0) {
            int val1 = dp(l + 1, r, 0) + (int)(a[l] != a[l + 1]);
            int val2 = dp(l + 1, r, 1) + (int)(a[l] != a[r]);
            val = min(val1, val2);
        } else {
            int val1 = dp(l, r - 1, 0) + (int) (a[r] != a[l]);
            int val2 = dp(l, r - 1, 1) + (int) (a[r] != a[r - 1]);
            val = min(val1, val2);
        }
        
        return memo[l][r][x] = val;
    };


    int ans1 = dp(0, n - 1, 1);
    int ans2 = dp(0, n - 1, 0);
    cout << min(ans1, ans2) << endl;
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