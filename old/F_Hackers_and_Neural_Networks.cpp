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
    vector<string> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    vector<int> ok(n, 0);
    int mn = n;
    for (int j = 0; j < m; j++) {
        vector<string> b(n);
        int cur = 0;
        for (int i = 0; i < n; i++) {
            cin >> b[i];
            if (b[i] != a[i]) {
                cur++;
            } else {
                ok[i] = 1;
            }
        }   
        mn = min(mn, cur);
    }
   
    if (count(ok.begin(), ok.end(), 0) != 0) {
        cout << -1 << endl;
        return;
    }

    cout << 2 * mn + n << endl;

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