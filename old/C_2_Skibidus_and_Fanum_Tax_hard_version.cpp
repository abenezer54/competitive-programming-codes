#include "bits/stdc++.h"
#ifndef ONLINE_JUDGE
#include "debug/debug.h"
#endif
using namespace std;
typedef long long ll;

void solve() {
    int n, m; cin >> n >> m;
    vector<int> a(n);
    for (auto& x: a){
        cin >> x;
    }
    
    vector<int> b(m);
    for (auto& x: b){
        cin >> x;
    }
    sort(b.begin(), b.end());

    a[0] = min(a[0], b[0] - a[0]);

    for (int i = 1; i < n; i++){
        int target = a[i - 1] + a[i];
        int idx = lower_bound(b.begin(), b.end(), target) - b.begin();
        if (idx >= m)
            continue;

        int mn = min(a[i], b[idx] - a[i]);
        int mx = max(a[i], b[idx] - a[i]);
        if (mn >= a[i - 1]){
            a[i] = mn;
        } else {
            a[i] = mx;
        }
    }

    for (int i = 1; i < n; i++){
        if (a[i] < a[i - 1]){
            cout << "NO" << '\n';
            return;
        }
    }

    cout << "YES" << '\n';
   
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