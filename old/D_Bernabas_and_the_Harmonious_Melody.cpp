#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n;
    cin >> n;
    string s;
    cin >> s;

    int ans = MOD;
    for (int i = 0; i < 26; i++) {
        int l = 0, r = s.size() - 1;
        int cur = 0;
        while (l < r) {
            if (s[l] == s[r]) {
                l++;
                r--;
            } else if (s[l] == 'a' + i) {
                l++;
                cur++;
            } else if (s[r] == 'a' + i) {
                r--;
                cur++;
            } else {
                break;
            }
        }
        if (l >= r) {
            ans = min(ans, cur);
        }
    }
    if (ans == MOD) {
        cout << -1 << endl;
    } else {
        cout << ans << endl;
    }
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