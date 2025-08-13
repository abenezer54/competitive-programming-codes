#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    string s;
    cin >> s;
    int n = s.size();
    s.push_back('*');
    int cur = 1;
    vector<int> val;
    for (int i = 1; i <= n; i++) {
        if (s[i] != s[i - 1]) {
            val.push_back(cur);
            cur = 0;
        }
        cur++;
    }
    ll ans = 1;
    for (auto v : val) {
        ans = (ll)ans * v;
    }
    for (int i = 0; i < 26; i++) {
        ans = max(ans, count(s.begin(), s.end(), 'a' + i));
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