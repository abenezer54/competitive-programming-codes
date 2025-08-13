#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    ll n, k; cin >> n >> k;

    vector<ll> a(n), b(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }

    unordered_map<ll, ll> cnt;

    for (int i = 0; i < n; i++) {
        ll r = a[i] % k;
        ll r2 = k - r;
        cnt[r]++;
        cnt[r2]++;
    }
    for (int i = 0; i < n; i++) {
        ll r = b[i] % k;
        ll r2 = k - r;
        if (cnt[r] == 0) {
            cout << "NO" << endl;
            return;
        }
        cnt[r]--;
        cnt[r2]--;
    }
    cout << "YES" << endl;

   
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