#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n; cin >> n;
    vector<int> a(n);
    // cout << abs(3 - 8) << endl;
    for (auto &x: a) cin >> x;
    // cout << a << endl;

    for (int i = 0; i < n - 1; i++){
        // for (int j = i + 1; j < n; j++){
            if (!(abs(a[i] - a[i + 1]) == 5 || abs(a[i] - a[i + 1]) == 7)) {
                // cout << a[i] << ' ' << a[j] << '\n';
                cout << "NO" << '\n';
                return;
            }
        // }
    }
    cout << "YES" << '\n';
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