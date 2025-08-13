#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;
const int MOD = 1e9 + 7;
int atleastK(string s, int val) {
    pair<int, int> x;
    x =  make_pair(1, 2);
    int l = 0;
    ll res = 0;
    int cnt = 0;
    for (int r = 0; r < s.size(); r++) {
        if (s[r] == '1')
            cnt++;
        if (cnt == val) {
            while (cnt == val) {
                if (s[l] == '1') {
                    cnt--;
                }
                l++;
            }
            res += (ll)((l + 2) * (s.size() - r + 1));
        }
    }
    return res;
}

void solve() {
    int k;
    cin >> k;
    string s;
    cin >> s;
    cout << atleastK(s, k) << endl;
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