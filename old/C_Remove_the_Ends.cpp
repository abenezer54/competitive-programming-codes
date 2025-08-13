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
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    vector<ll> p(n + 1, 0);
    vector<ll> s(n + 1, 0);
    for (int i = n - 1; i >= 0; i--) {
        if (a[i] < 0) {
            s[i] = s[i + 1] + abs(a[i]);
        } else {
            s[i] = s[i + 1];
        }
    }

    for (int i = 1; i <= n; i++) {
        if (a[i - 1] > 0) {
            p[i] = a[i - 1] + p[i - 1];
        } else {
            p[i] = p[i - 1];
        }
    }
    // cout << p << endl;
    // cout << s << endl;
    ll ans = 0;
    for (int i = 0; i < n; i++) {
        ll val1 = p[i] + s[i];
        ll val2 = p[i + 1] + s[i + 1];
        ans = max({ans, val1, val2});
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