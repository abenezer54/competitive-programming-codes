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
    int ans = n - 1;
    for (int i = 0; i < n; i++) {
        if (s[i] != '0') {
            int cnt = 0; 
            for (int j = 0; j < n; j++) {
                cnt += (j < i && s[j] != '0'); 

                cnt += (j > i);
            }

            ans = min(ans, cnt);
        }
    }
    cout << ans << endl; 
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