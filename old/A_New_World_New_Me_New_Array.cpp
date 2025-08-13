#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
   
    int n, k, p; cin >> n >> k >> p;

    k = abs(k);
    if (n * p < k) {
        cout << -1 << endl;
        return;
    }

    cout << (k + (p - 1)) / p << endl;
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