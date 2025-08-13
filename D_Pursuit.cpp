#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll n; cin >> n;
    vector<ll> a(n), b(n);
    for (ll i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (ll i = 0; i < n; i++) {
        cin >> b[i];
    }

    sort(a.rbegin(), a.rend());
    sort(b.rbegin(), b.rend());

    ll cur_len = n - (n / 4);
    ll a_score = 0, b_score = 0;
    for (ll i = 0; i < cur_len; i++) {
        a_score += a[i];
        b_score += b[i];
    }



    auto check = [&] (ll x) {
        ll new_n = x + n;
        ll new_len = new_n - (new_n / 4);
        ll new_a = 0ll, new_b = 0ll;
        ll mn = min(new_len, x);
        new_a += mn * 100;
        for (int i = 0; i < min(new_len - mn, n); i++) {
            new_a += a[i];
        }
        for (int i = 0; i < min(new_len, n); i++) {
            new_b += b[i];
        }
        return new_a >= new_b;

    };

    ll l = -1, r = 1e7 + 10;
    while (l + 1 < r) {
        ll mid = l + (r - l) / 2;
        if (check(mid)) {
            r = mid;
        } else {
            l = mid;
        }
    }
    cout << r << endl;

    
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