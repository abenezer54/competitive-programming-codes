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
    vector<int> b(n), w(m);
    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }

    for (int i = 0; i < m; i++) {
        cin >> w[i];
    }
    sort(b.rbegin(), b.rend());
    sort(w.rbegin(), w.rend());

    int i = 0, j = 0;
    ll ans = 0;
    while (i < n && j < m) {
        if (b[i] + w[i] > 0 && w[i] > 0) {
            ans += b[i] + w[i];
            i++;
            j++;
        } else {
            break;
        }
    }

    while (i < n && b[i] > 0) {
        ans += b[i];
        i++;
    }
    cout << ans << endl;

   
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