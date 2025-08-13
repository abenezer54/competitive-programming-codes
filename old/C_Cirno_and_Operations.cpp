#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;


void solve() {
    int n; cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    ll ans = accumulate(a.begin(), a.end(), 0LL);
    while (a.size() > 1) {
        vector<ll> temp;
        for (int i = 0; i < a.size() - 1; i++) {
            temp.push_back(a[i] - a[i + 1]);
        }
   
        ll cur = accumulate(temp.begin(), temp.end(), 0LL);
        ans = max(ans, abs(cur));
        a = temp;
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