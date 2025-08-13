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
    vector<int> a(n), b(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }


    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    if (a[0] != b[0]) {
        cout << "NO" << endl;
        return;
    }

    int prev1 = a[0], prev2 = a[0];
    for (int i = 1; i < n; i++) {
        int target = 0;
        for (int bit = 0; bit < 32; bit++) {
            int x = a[i] & (1 << bit);
            int y = b[i] & (1 << bit);
            if (y != x) {
                target |= (1 << bit);
            }
            // if (y == 0 && x )
        }
        // cout << "i: " << i  << " target:  " << target << " prev1 " << prev1 << " prev2: " << prev2 << endl;
        if (!(target == prev1 || target == prev2) && target) {
            cout << "NO" << endl;
            return;
        }
        prev1 = a[i];
        prev2 = b[i];
    }
    cout << "YES " << endl;
   
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