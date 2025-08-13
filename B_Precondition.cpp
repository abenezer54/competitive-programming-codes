#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    string s, t;
    cin >> s >> t;

    auto x = find(s.begin(), s.end(), 'a');
    for (int i = 1; i < s.size(); i++) {
        if (isupper(s[i]) && find(t.begin(), t.end(), s[i - 1]) == t.end()) {
            cout << "No" << endl;
            return;
        }
    }    

    cout << "Yes" << endl;
   
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