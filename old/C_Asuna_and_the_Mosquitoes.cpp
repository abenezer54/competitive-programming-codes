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
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());
    vector<ll> odd, even;

    for (auto val: a) {
        if (val % 2 == 1) {
            odd.push_back(val);
        }
        else {
            even.push_back(val);
        }
    }

    if (odd.size() == 0 || even.size() == 0) {
        cout << a.back() << endl;
        return;
    }
    ll mx = a.back();
    ll cur = 0;
    for (int i = 0; i < odd.size() - 1; i++) {
        cur += odd[i] - 1;
    }
    if (odd.size() > 1 && cur > 1) {
        cur += 1;
    }
    cur += accumulate(even.begin(), even.end(), 0LL);
    if (odd.size() > 1) {
        cur -= 1;
    }
    cout << cur + mx << endl;
    
    

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