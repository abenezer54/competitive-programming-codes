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
    vector<ll> a(n); for (int i = 0; i < n; i++) cin >> a[i];
    if (k >= 3) {
        cout << 0 << endl;
        return;
    }
    sort(a.begin(), a.end());
    
    ll ans = a[0];
    vector<ll> temp;
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            temp.push_back(abs(a[j] - a[i]));
        }
    }

    ll mn = *min_element(temp.begin(), temp.end());
    ans = min(mn, ans);
    if (k == 1) {
        cout << ans << endl;
        return;
    }

    for (int i = 0; i < temp.size(); i++) {
        int j = upper_bound(a.begin(), a.end(), temp[i]) - a.begin();
        if (j - 1 >= 0) {
            ans = min(ans, abs(a[j - 1] - temp[i]));
        }
        if (j < n) {
            ans = min(ans, abs(a[j] - temp[i]));
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