#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n, k, q; cin >> n >> k >> q;
    vector<vector<int>> a(k, vector<int>(n));
    for(int i = 0; i < n; i++){
        for(int j = 0; j < k; j++){
            cin >> a[j][i];
        }
    }
    for(int j = 0; j < k; j++){
        for(int i = 1; i < n; i++){
            a[j][i] |= a[j][i - 1];
        }
    }
    
    for (int i = 0; i < q; i++){
        int m; cin >> m;
        int lower = 0, upper = n - 1;
        for (int j = 0; j < m; j++){
            int r, val;
            char o;
            cin >> r >> o >> val;
            r--;

            if (o == '>')
            {
                int idx = upper_bound(a[r].begin(), a[r].end(), val) - a[r].begin();
                lower = max(lower, idx);
            } 
            else
            {
                int idx = lower_bound(a[r].begin(), a[r].end(), val) - a[r].begin() - 1;
                upper = min(upper, idx);
            }
        }
        cout << (upper >= lower ? lower + 1 : -1) << '\n';

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