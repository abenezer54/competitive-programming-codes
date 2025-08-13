#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int a, b, c; cin >> a >> b >> c;

    if (a > max(c, b)) {
        cout << 0 << ' ';
    } else {
        cout << max(c, b) - a + 1 << ' ';
    }
    if (b > max(c, a)) {
        cout << 0 << ' ';
    } else {
        cout << max(c, a) - b + 1 << ' ';
    }
    if (c > max(b, a)) {
        cout << 0 << ' ';
    } else {
        cout << max(b, a) - c + 1 << ' ';
    }
    cout << '\n';

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