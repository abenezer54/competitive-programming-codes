#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    string s; cin >> s;
    int ans = 0;
    int i = 0;
    int cnt = 0;
    while (i < s.size()) {
        if (cnt % 2 == 0) {
            if (s[i] == 'i') {
                i++;
            } else {
                ans++;
            }
        } else {
            if (s[i] == 'o') {
                i++;
            } else {
                ans++;
            }
        }
        cnt++;
    }
    
    if ((ans + s.size()) % 2 == 1) ans++;
    cout << ans << endl;
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