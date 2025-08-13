#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {

    int x; cin >> x;
    int bit_count = log2(x);
    int y = (1 << bit_count) - 1;
    int xy = (x ^ y);
    if (x + y > xy && xy + x > y && xy + y > x) {
        cout << y << endl;
    } else {
        cout << -1 << endl;
    }

   
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