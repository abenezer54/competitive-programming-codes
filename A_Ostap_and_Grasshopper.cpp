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
    string s; cin >> s;

    int x = 0;
    int idx = -1;
    
    for (int i = 0; i < n; i++) {
        
        if ((x & 1) && s[i] == '#' && (i - idx) % k == 0) {
            cout << "NO" << endl;
            return;
        }
        if ((x & 1) && (s[i] == 'G' || s[i] == 'T') && (i - idx) % k != 0) {
            cout << "NO" << endl;
            return;
        }
        if (s[i] == 'G' || s[i] == 'T') {
            x++;
            idx = i;
        }

    }
    cout << "YES" << endl;
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