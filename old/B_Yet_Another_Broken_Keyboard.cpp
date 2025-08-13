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
    set<char> check;
    for (int i = 0; i < n; i++) {
        char c; cin >> c;
        check.insert(c);
    }   

    int last = -1;
    ll ans =  ((ll)n * (n + 1)) / 2;
    for (int i = 0; i < n; i++) {
        if (!check.count(s[i])) {
            ans -= (ll) (i - last) * (n - i);
            last = i;
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