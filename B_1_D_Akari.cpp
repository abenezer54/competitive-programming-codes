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

    int prev = 0;
    for (int i = 1; i < s.size(); i++) {
        if (s[i] == '#' && s[i - 1] == '.') {
            s[i - 1] = 'o';
        }
    }
    if (s[s.size() - 1]== '.') {
        s[s.size() - 1] = 'o';
    }
    cout << s << endl;
   
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