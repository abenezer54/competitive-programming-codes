#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, m; cin >> n >> m;
    vector<string>a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int ans = 0;
    for (int i = 0; i < n; i++) {
        int x = 0;
        for (int j = 0; j < m; j++) {
            x += a[i][j] - '0';
        }
        // cout << "row " << i << ' ' << x << endl;

        if (x & 1) {
            bool found = false;
            for (int j = 0; j < m; j++) {
                int y = 0;
                for (int k = 0; k < n; k++) {
                    y += a[k][j] - '0';
                }

                if (y & 1) {
                    a[i][j] = (a[i][j] == '1' ? '0': '1');
                    found = true;
                    ans++;
                }
                
            }
            if (found) {
                // ans++;
            } else {
                for (int j = 0; j < m; j++) {
                    ans += a[i][j] - '0';
                    a[i][j] = 0;
                }
            }
        }
    }
    // cout << a << endl;
    cout << ans << endl;


   
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