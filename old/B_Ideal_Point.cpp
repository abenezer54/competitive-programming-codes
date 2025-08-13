#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, k; cin >> n >> k;
    int x = 0, y = 0;
    for (int i = 0; i < n; i++) {
        int a, b; cin >> a >> b;
        x += a == k;
        y += b == k;
    }

    if (x && y) cout << "YES" << endl;
    else cout << "NO" << endl;
   
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