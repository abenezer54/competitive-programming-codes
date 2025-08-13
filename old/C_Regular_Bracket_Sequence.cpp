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
    int n = s.size();
    vector<int> stk;
    int ans = 0;
    for (int i = 0; i < n; i ++) {
        if (s[i] == '(') {
            stk.push_back(i);
        } else {
            if (stk.empty()) {
                ans++;
            } else {
                stk.pop_back();
            }
        }
    }
    cout << n - (ans + stk.size()) << endl;
   
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