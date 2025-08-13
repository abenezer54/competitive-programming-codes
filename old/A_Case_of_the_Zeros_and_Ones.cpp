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
    string s; cin >> s;
    vector<char> stk;
    int ans = n;
    for (int i = 0; i < n; i++) {
        if (stk.empty()) {
            stk.push_back(s[i]);
        } else {
            if (stk.back() != s[i]) {
                stk.pop_back();
                ans -= 2;
            } else {
                stk.push_back(s[i]);
            }
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