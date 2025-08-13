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
    vector<ll> a(n * 2);
    for (ll i = 0; i < 2 * n; i++) {
        cin >> a[i];
    }   
    map<array<ll, 2>, ll> prev;
    ll ans = 0;
    for (ll i = 0; i < 2 * n - 1; i++) {
        array<ll, 2> key1 = {a[i], a[i + 1]};
        array<ll, 2> key2 = {a[i + 1], a[i]};

            if (a[i] == a[i + 1]) continue;
            if ((i > 0 && a[i] == a[i - 1])) continue;

        if ((prev.count(key1) && i - prev[key1] > 1) ||(prev.count(key2) && i - prev[key2] > 1)) {
            ans++;
        }

        if (!prev.count(key1)) {
            prev[key1] = i;
        } 

        if (!prev.count(key2)){
            prev[key2] = i;
        }
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