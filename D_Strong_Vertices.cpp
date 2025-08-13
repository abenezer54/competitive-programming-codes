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

    vector<int> a(n), b(n), diff(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }
    for (int i = 0; i < n; i++) {
        diff[i] = a[i] - b[i];
    }
    int mx = *max_element(diff.begin(), diff.end());

    vector<int> ans;
    for (int i = 0; i < n; i++) {
        if (diff[i] == mx) {
            ans.push_back(i + 1);
        }
    }
    sort(ans.begin(), ans.end());
    cout << ans.size() << endl;

    for (auto node: ans) {
        cout << node << ' ';
    }

    cout << endl;
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