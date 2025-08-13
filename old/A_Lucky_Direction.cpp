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
    map<char, char> mp = {{'N', 'S'}, {'S', 'N'}, {'E', 'W'}, {'W', 'E'}};
    string ans;
    for (char c: s) {
        ans += mp[c];
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