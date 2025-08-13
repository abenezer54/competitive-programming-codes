#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
#define endl '\n'
typedef long long ll;
const int MOD = 1e9 + 7;

void solve() {
    int n, q; cin >> n >> q;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int mx = *max_element(a.begin(), a.end());
    int idx = 0;
    map<int, array<int, 2>> pre;
    int cur_mx = a[0];
    vector<int> temp;
    for (int i = 0; i < n; i++) {
        if (i > 0) {
            pre[i] = {cur_mx, a[i]};
            temp.push_back(min(a[i], cur_mx));
            cur_mx = max(cur_mx, a[i]);
        }
        if (a[i] == mx) {
            idx = i;
            break;
        }
    }

    vector<int> ans;
    for (int i = idx + 1; i < n; i++) {
        ans.push_back(a[i]);
    }
    for (int val: temp) {
        ans.push_back(val);
    }

    for (int i = 0; i < q; i++) {
        ll m; cin >> m;
        if (m <= idx) {
            cout << pre[m][0] << ' ' << pre[m][1] << endl;
        } else {
            m -= idx;
            int val = (m % (n - 1));
            if (val == 0) val = n - 1;
            val--;
            cout << mx << ' ' << ans[val] << endl;
        }
    }
   
    
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