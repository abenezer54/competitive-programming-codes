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
    int ans = 1e9;
    for (int i = 0; i < 26; i++) {
        vector<int> idx = {-1};
        for (int j = 0; j < n; j++) {
            if (s[j] - 'a' == i) {
                idx.push_back(j);
            }
        }
        idx.push_back(n);
        int mx = 0;
        for (int j = 1; j < idx.size(); j++) {
            mx = max(mx, idx[j] - idx[j - 1]);
        }
        ans = min(ans, mx);

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