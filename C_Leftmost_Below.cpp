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
    int x = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    int mn = a[0];
    for (int i = 1; i < n; i++) {
        mn = min(mn, a[i]);
        // cout << mn << endl;
        if (a[i] > 1 && (a[i] > (mn*2) - 1)) {
            cout << "NO" << endl;
            return;
        }

    }
    cout << "YES" << endl;

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