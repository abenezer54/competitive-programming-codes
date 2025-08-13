#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, l, r;
    cin >> n >> l >> r;

    string s; cin >> s;
    string ans = "Yes";
    for (int i = l - 1; i < r; i++) {
        if (s[i] == 'x') {
            ans = "No";
        } 
    }
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