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
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    ll tot = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            tot += a[j] < a[i];
        }
    }
    ll mn = tot;
    vector<int> ans = {1, 1};
    for (int i = 0; i < n; i++) {
        ll cur = tot;
        for (int j = i + 1; j < n; j++) {
            if (a[j] > a[i]) {
                cur++;
            } else if (a[j] < a[i]) {
                cur--;
            }
            if (cur < mn) {
                mn = cur;
                ans = {i + 1, j + 1};
            }
        }
    }

    cout << ans[0] << ' ' << ans[1] << endl;


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