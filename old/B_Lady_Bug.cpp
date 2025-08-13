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
    string a, b; cin >> a >> b;
    int x = 0, y = 0;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            x += a[i] == '0';
            y += b[i] == '0';
        } else {
            x += b[i] == '0';
            y += a[i] == '0';
        }
    }

    // cout << x << ' ' << y << endl;
    int half = n / 2;
    int fhalf = half + (n & 1);
    if (x >= fhalf && y >= half) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
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