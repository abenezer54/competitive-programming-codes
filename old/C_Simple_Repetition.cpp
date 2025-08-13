#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;


void solve() {
    int x, k; cin >> x >> k;
    if (x >= 2 && k >= 2) {
        cout << "NO" << endl;
        return;
    }

    if (x == 1) {
        cout << (k == 2 ? "YES" : "NO") << endl;
        return;
    } 

    for (int i = 2; i <= (int) sqrt(x); i++) {
        if (x % i == 0) {
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